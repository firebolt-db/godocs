#!/usr/bin/env python3
import json
import pathlib
import pprint
import re
from typing import Iterator


class LostPagesError(Exception):
    pass


def group_collect_pages(pages) -> Iterator[str]:
    if not isinstance(pages, list):
        raise LostPagesError(f"Expected a list of pages, got {type(pages)}: {pprint.pformat(pages)}")
    if not pages:
        raise LostPagesError(f"Expected at least one page, got {len(pages)}")
    for p in pages:
        if isinstance(p, str):
            yield p
        elif isinstance(p, dict):
            if "groups" in p:
                yield from group_collect_pages(p["groups"])
            elif "pages" in p:
                yield from group_collect_pages(p["pages"])
            elif "href" in p:
                continue
            elif "openapi" in p:
                continue
            else:
                raise LostPagesError(f"Unexpected entry: {p}")
        else:
            raise LostPagesError(f"Unexpected entry: {p}")


def check_lost_pages(docs_dir: pathlib.Path, tabs: list, hidden_pages: list) -> None:
    navigatable_pages = set(f"{p}.mdx" for p in group_collect_pages(tabs))

    exceptions = set()
    for page in hidden_pages:
        if not page.get("path"):
            raise LostPagesError(f"Expected a page with 'path' key, got {page}")
        if not page.get("reason"):
            raise LostPagesError(f"Expected a page with 'reason' key, got {page}")
        exceptions.add(page["path"])

    if stale_exceptions := exceptions & navigatable_pages:
        raise LostPagesError(
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
        raise LostPagesError(
            f"Found {len(stale_exceptions)} pages that are listed in hidden but do not exist:\n"
            + "\n".join(sorted(stale_exceptions))
        )

    if stale_unindexed := unindexed_pages & navigatable_pages:
        raise LostPagesError(
            f"Found {len(stale_unindexed)} pages that are marked as noindex but are in the navigation:\n"
            + "\n".join(sorted(stale_unindexed))
        )

    lost_pages -= {"index.mdx"}
    lost_pages -= exceptions
    if lost_pages:
        raise LostPagesError(
            f"Found {len(lost_pages)} pages that are not navigatable:\n"
            + "\n".join(sorted(lost_pages))
        )


def main(root_dir: pathlib.Path):
    docs_dir = root_dir / 'docs-mdx'
    docs_json = json.loads((docs_dir / 'docs.json').read_text())
    hidden_pages = json.loads((root_dir / "hidden_pages.json").read_text())
    check_lost_pages(docs_dir, docs_json["navigation"]["tabs"], hidden_pages)


if __name__ == "__main__":
    main(pathlib.Path(__file__).parent.parent)
