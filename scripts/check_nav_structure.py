#!/usr/bin/env python3
import json
import pathlib
import pprint
import re
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
    exceptions = {
        "index.mdx",
        "reference/proof-of-concept-guide.mdx",

        # TODO: these are lost pages:
        'guides/operate-engines/working-with-engines-using-the-firebolt-manager.mdx',
        'guides/query-data/keyboard-shortcuts-for-sql-editor.mdx',
        'overview/choosing-an-engine.mdx',
        'reference-sql/bytea-data-type.mdx',
        'reference-sql/date-data-type.mdx',
        'reference-sql/functions-reference/aggregate-array.mdx',
        'reference-sql/functions-reference/aggregate-array/array-count-global.mdx',
        'reference-sql/functions-reference/aggregate-array/array-max-global.mdx',
        'reference-sql/functions-reference/aggregate-array/array-min-global.mdx',
        'reference-sql/functions-reference/aggregate-array/array-sum-global.mdx',
        'reference-sql/functions-reference/aggregation/approx-percentile.mdx',
        'reference-sql/functions-reference/aggregation/percentile-disc.mdx',
        'reference-sql/functions-reference/array/array-cumulative-sum.mdx',
        'reference-sql/functions-reference/array/array-fill.mdx',
        'reference-sql/functions-reference/array/array-first-index.mdx',
        'reference-sql/functions-reference/array/array-replace-backwards.mdx',
        'reference-sql/functions-reference/array/array-slice.mdx',
        'reference-sql/functions-reference/date-and-time/date-diff.mdx',
        'reference-sql/functions-reference/numeric/cbrt.mdx',
        'reference-sql/functions-reference/numeric/exp.mdx',
        'reference-sql/functions-reference/numeric/sign.mdx',
        'reference-sql/functions-reference/numeric/trunc.mdx',
        'reference-sql/functions-reference/string/base64-encode.mdx',
        'reference-sql/functions-reference/string/extract-all.mdx',
        'reference-sql/functions-reference/string/match-any.mdx',
        'reference-sql/functions-reference/string/match.mdx',
        'reference-sql/functions-reference/string/md5-number-lower64.mdx',
        'reference-sql/functions-reference/string/md5-number-upper64.mdx',
        'reference-sql/functions-reference/string/md5.mdx',
        'reference-sql/functions-reference/string/repeat.mdx',
        'reference-sql/functions-reference/string/reverse.mdx',
        'reference-sql/functions-reference/string/split.mdx',
        'reference-sql/functions-reference/string/to-double.mdx',
        'reference-sql/functions-reference/string/to-float.mdx',
        'reference-sql/functions-reference/string/to-int.mdx',
        'reference-sql/functions-reference/window/cume-dist.mdx',
        'reference-sql/functions-reference/window/nth-value.mdx',
        'reference-sql/functions-reference/window/percentile-cont-window.mdx',
        'reference-sql/functions-reference/window/percentile-disc-window.mdx',
        'reference-sql/geography-data-type.mdx',
        'reference-sql/numeric-data-type.mdx',
        'reference-sql/struct-data-type.mdx',
        'reference-sql/timestampntz-data-type.mdx',
        'reference-sql/timestamptz-data-type.mdx',
        'reference/interval-arithmetic.mdx',
    }

    lost_pages = []
    for p in docs_dir.glob("**/*.mdx"):
        rel_p = p.relative_to(docs_dir)
        if len(rel_p.parents) > 1 and rel_p.parents[-2].name == "snippets":
            continue
        if str(rel_p) in exceptions:
            continue
        if not str(p.relative_to(docs_dir)) in navigatable_pages:
            lost_pages.append(str(rel_p))

    lost_pages.sort()
    if lost_pages:
        print(f"Found {len(lost_pages)} hidden pages:")
        for p in lost_pages:
            print(f'{repr(p)},')
        raise Exception(
            f"Found {len(lost_pages)} pages that are not navigatable:\n"
            + "\n".join(f"https://docs.firebolt.io/{p.removesuffix('.mdx')}" for p in sorted(lost_pages))
        )


def check_group_structure(parent, pages) -> None:
    if not isinstance(pages, list):
        raise ValueError(f"Expected a list of pages, got {type(pages)}: {pprint.pformat(pages)}")
    if not pages:
        raise ValueError(f"Expected at least one page, got {len(pages)}")
    if isinstance(pages[0], str):
        dir_page = pages[0]
        if parent:
            if not re.match(f'^{parent}/[^/]+$', dir_page):
                raise ValueError(f"Expected first page in the group to be under {parent}, got {dir_page}")
        else:
            if not re.match(r'^[^/]+$', dir_page):
                raise ValueError(f"Expected the first page in the group to be a top-level page, got {dir_page}")
    else:
        dir_page = ""
    for p in pages:
        if isinstance(p, str):
            if not dir_page:
                raise ValueError(f"Expected the first page in the group to be a top-level page, got {p}")
            if not (p == dir_page or re.match(f'^{dir_page}/[^/]+$', p)):
                raise Exception(f"Expected all pages in the group to be under {dir_page}, got {p}")
        elif isinstance(p, dict):
            if "pages" in p:
                check_group_structure(dir_page or parent, p["pages"])
            elif "href" in p:
                continue
            else:
                raise ValueError(f"Unexpected entry: {p}")
        else:
            raise ValueError(f"Unexpected entry: {p}")


def main():
    docs_dir = pathlib.Path(__file__).parent.parent / 'docs-mdx'
    docs_json = json.loads((docs_dir / 'docs.json').read_text())

    check_lost_pages(docs_dir, docs_json["navigation"]["tabs"])
    check_group_structure("", docs_json["navigation"]["tabs"])


if __name__ == "__main__":
    main()
