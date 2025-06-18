#!/usr/bin/env python3
import json
import pathlib
import pprint
import re
import string
from typing import Iterator


def group_collect_pages(pages) -> Iterator[str]:
    if not isinstance(pages, list):
        raise ValueError(f"Expected a list of pages, got {type(pages)}: {pprint.pformat(pages)}")
    if not pages:
        raise ValueError(f"Expected at least one page, got {len(pages)}")
    for p in pages:
        if isinstance(p, str):
            yield p
        elif isinstance(p, dict):
            if "pages" in p:
                yield from group_collect_pages(p["pages"])
            elif "href" in p:
                continue
            else:
                raise ValueError(f"Unexpected entry: {p}")
        else:
            raise ValueError(f"Unexpected entry: {p}")


def check_lost_pages(docs_dir: pathlib.Path, tabs: list) -> None:
    navigatable_pages = set(f"{p}.mdx" for p in group_collect_pages(tabs))
    hidden_pages = json.loads((pathlib.Path(docs_dir).parent / "hidden-pages.json").read_text())
    exceptions = set()
    for page in hidden_pages:
        if not page.get("path"):
            raise ValueError(f"Expected a page with 'path' key, got {page}")
        if not page.get("reason"):
            raise ValueError(f"Expected a page with 'reason' key, got {page}")
        exceptions.add(page["path"])

    if stale_exceptions := exceptions & navigatable_pages:
        raise Exception(
            f"Found {len(stale_exceptions)} pages that are listed in hidden but are in the navigation:\n"
            + "\n".join(sorted(stale_exceptions))
        )

    lost_pages = set()
    unindexed_pages = set()
    for p in docs_dir.glob("**/*.mdx"):
        rel_p = p.relative_to(docs_dir)
        if len(rel_p.parents) > 1 and rel_p.parents[-2].name == "snippets":
            continue
        if not str(p.relative_to(docs_dir)) in navigatable_pages:
            lost_pages.add(str(rel_p))
        if re.match("^---\n.*?(groups:\\s+\\[\\s*\\]|noindex:\\s+true)\\s*?\n.*?---\n", p.read_text(), re.DOTALL):
            unindexed_pages.add(str(rel_p))

    if stale_exceptions := exceptions - lost_pages:
        raise Exception(
            f"Found {len(stale_exceptions)} pages that are listed in hidden but do not exist:\n"
            + "\n".join(sorted(stale_exceptions))
        )

    if stale_unindexed := unindexed_pages & navigatable_pages:
        raise Exception(
            f"Found {len(stale_unindexed)} pages that are marked as noindex but are in the navigation:\n"
            + "\n".join(sorted(stale_unindexed))
        )

    lost_pages -= {"index.mdx"}
    lost_pages -= exceptions
    if lost_pages:
        raise Exception(
            f"Found {len(lost_pages)} pages that are not navigatable:\n"
            + "\n".join(sorted(lost_pages))
        )


def check_group_structure(pages: list[str|dict], level: int) -> list[str]:
    if not isinstance(pages, list):
        raise ValueError(f"Expected a list of pages, got {type(pages)}: {pprint.pformat(pages)}")
    if not pages:
        raise ValueError(f"Expected at least one page in the group")

    common_path = None
    for p in pages:
        if isinstance(p, str):
            if p.startswith("/") or p.endswith("/") or set(p).intersection(set(" ." + string.ascii_uppercase)):
                raise ValueError(f"Page address is not allowed: {p}")
            p_parts = p.split("/")
            if common_path is None:
                common_path = p_parts[:level]
            if p_parts[:level] != common_path:
                raise ValueError(f"Expected all pages in the group to have the same path prefix, got {p} with prefix {p_parts[:level]} instead of {common_path}")
        elif isinstance(p, dict):
            if "pages" in p:
                sub_common_path = check_group_structure(p["pages"], level + 1)
                if common_path is None:
                    common_path = sub_common_path[:level]
                elif sub_common_path[:level] != common_path:
                    raise ValueError(f"Expected all pages in the group to have the same path prefix, got {p} with prefix {sub_common_path} instead of {common_path}")
            elif "href" in p:
                continue
            else:
                raise ValueError(f"Unexpected entry: {p}")
        else:
            raise ValueError(f"Unexpected entry: {p}")
    if common_path is None:
        raise ValueError("Expected at least one page in the group")
    return common_path


def main():
    docs_dir = pathlib.Path(__file__).parent.parent / 'docs-mdx'
    docs_json = json.loads((docs_dir / 'docs.json').read_text())

    check_lost_pages(docs_dir, docs_json["navigation"]["tabs"])
    check_group_structure(docs_json["navigation"]["tabs"], -1)


if __name__ == "__main__":
    main()
