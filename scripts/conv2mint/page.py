import re
import dataclasses
import pathlib
import yaml

import utils


@dataclasses.dataclass(kw_only=True, frozen=True)
class FrontMatterJekyll:
    title: str | None = None
    parent: str | None = None
    nav_order: int | None = None
    description: str | None = None
    layout: str | None = None
    permalink: str | None = None
    redirect_from: list[str] | None = None
    has_children: bool | None = None
    redirect_to: str | None = None
    nav_exclude: bool | None = None
    search_exclude: bool | None = None
    sitemap: bool | None = None
    published: bool | None = None
    # useless fields
    has_toc: bool | None = None
    grand_parent: str | None = None
    great_grand_parent: str | None = None


@dataclasses.dataclass(kw_only=True, frozen=True)
class FrontMatterMint:
    title: str | None = None
    description: str | None = None
    sidebarTitle: str | None = None
    icon: str | None = None
    iconType: str | None = None
    mode: str | None = None
    url: str | None = None
    groups: list[str] | None = None
    # openapi: str | None = None
    # keywords: list[str] | None = None
    # meta_tags: dict[str, str] | None = None


@dataclasses.dataclass(kw_only=True, frozen=True)
class ParsedPage:
    rel_path: pathlib.Path
    fm: FrontMatterJekyll | None
    content: str


@dataclasses.dataclass(kw_only=True)
class ConvertedPage:
    src: ParsedPage
    fm: FrontMatterMint
    content: str


def parse_page(page: str, rel_path: pathlib.Path) -> ParsedPage:
    """Parse a page from a string.
    >>> parse_page('---\\ntitle: bar\\n---\\n# Header\\nContent', pathlib.Path('path/to/file.md')).content
    '# Header\\nContent'
    >>> utils.filter_none(dataclasses.asdict(parse_page('---\\ntitle: bar\\n---\\n# Header\\nContent', pathlib.Path('path/to/file.md')).fm))
    {'title': 'bar'}
    >>> parse_page('---\\n---\\n# Header\\nContent', pathlib.Path('path/to/file.md')).content
    '# Header\\nContent'
    >>> utils.filter_none(dataclasses.asdict(parse_page('---\\n---\\n# Header\\nContent', pathlib.Path('path/to/file.md')).fm))
    {}
    """
    frontmatter_match = re.match(r'^---\n(.*?)---\n', page, re.DOTALL)
    if frontmatter_match is None:
        raise Exception(f"front matter not found in {rel_path}")
    fm = frontmatter_match.group(0)
    fm_yaml = frontmatter_match.group(1)
    fm_raw = yaml.safe_load(fm_yaml) or {}
    return ParsedPage(
        rel_path=rel_path,
        fm=FrontMatterJekyll(**fm_raw),
        content=page[len(fm):]
    )


def render_page(p: ConvertedPage) -> str:
    fm_dict = dataclasses.asdict(p.fm)
    for k in list(fm_dict.keys()):
        if fm_dict[k] is None:
            del fm_dict[k]
    fm_raw = yaml.dump(fm_dict, default_flow_style=False)
    return f"---\n{fm_raw}---\n{p.content}\n"
