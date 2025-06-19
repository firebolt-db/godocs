#!/usr/bin/env python3
import json
import pathlib
import pprint
import re
import string
from typing import Iterator


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
    root_dir = pathlib.Path(__file__).parent.parent
    docs_dir = root_dir / 'docs-mdx'
    docs_json = json.loads((docs_dir / 'docs.json').read_text())

    check_group_structure(docs_json["navigation"]["tabs"], -1)


if __name__ == "__main__":
    main()
