import re
import dataclasses
import pathlib
import yaml

import utils


@dataclasses.dataclass(kw_only=True, frozen=True)
class PageDescrJekyll:
    rel_path: pathlib.Path
    is_root: bool
    is_index: bool
    is_fragment: bool

    main_url: str | None = None
    all_urls: list[str] | None = None
    builtin_redirects: list[str] | None = None


@dataclasses.dataclass(kw_only=True)
class PageDescrMint:
    rel_path: pathlib.Path
    is_root: bool
    is_index: bool
    is_fragment: bool

    main_url: str | None = None


@dataclasses.dataclass(kw_only=True, frozen=True)
class FrontMatterJekyll:
    title: str | None = None
    description: str | None = None

    # all the redirects leading to the main url of the page
    redirect_from: list[str] | None = None

    # navigation structure fields
    parent: str | None = None
    grand_parent: str | None = None
    great_grand_parent: str | None = None
    nav_order: int | None = None

    # whether to output the list of child pages at the bottom of the page
    has_toc: bool | None = None

    # controlling the visibility of the page
    published: bool | None = None
    nav_exclude: bool | None = None
    search_exclude: bool | None = None

    # useless fields
    layout: str | None = None
    sitemap: bool | None = None
    has_children: bool | None = None

    # thankfully unused fields
    # permalink: str | None = None
    # redirect_to: str | None = None

    @property
    def is_published(self) -> bool:
        return self.published is not False

    @property
    def is_navigatable(self) -> bool:
        return self.is_published and not self.nav_exclude

    @property
    def is_searchable(self) -> bool:
        return self.is_published and not self.search_exclude


@dataclasses.dataclass(kw_only=True)
class FrontMatterMint:
    title: str | None = None
    description: str | None = None
    sidebarTitle: str | None = None
    mode: str | None = None
    groups: list[str] | None = None
    no_index: bool | None = None
    # icon: str | None = None
    # iconType: str | None = None
    # openapi: str | None = None
    # url: str | None = None
    # keywords: list[str] | None = None
    # meta_tags: dict[str, str] | None = None


@dataclasses.dataclass(kw_only=True, frozen=True)
class PageJekyll:
    descr: PageDescrJekyll
    fm: FrontMatterJekyll | None
    content: str


@dataclasses.dataclass(kw_only=True)
class PageMint:
    descr: PageDescrMint
    fm: FrontMatterMint | None
    content: str


def build_page_descr_jekyll(rel_path: pathlib.Path) -> PageDescrJekyll:
    """Build a page description from a relative path.
    >>> build_page_descr_jekyll(pathlib.Path("_includes/page.md"))
    PageDescrJekyll(rel_path=PosixPath('_includes/page.md'), is_root=False, is_index=False, is_fragment=True, main_url=None, all_urls=None, builtin_redirects=None)
    >>> build_page_descr_jekyll(pathlib.Path("page.md"))
    PageDescrJekyll(rel_path=PosixPath('page.md'), is_root=True, is_index=False, is_fragment=False, main_url='/page.html', all_urls=['/page.html', '/page'], builtin_redirects=[])
    >>> build_page_descr_jekyll(pathlib.Path("index.md"))
    PageDescrJekyll(rel_path=PosixPath('index.md'), is_root=True, is_index=True, is_fragment=False, main_url='/', all_urls=['/index.html', '/index', '/'], builtin_redirects=[])
    >>> build_page_descr_jekyll(pathlib.Path("subdir/index.md"))
    PageDescrJekyll(rel_path=PosixPath('subdir/index.md'), is_root=False, is_index=True, is_fragment=False, main_url='/subdir/', all_urls=['/subdir/index.html', '/subdir/index', '/subdir/'], builtin_redirects=['/subdir'])
    >>> build_page_descr_jekyll(pathlib.Path("subdir/page.md"))
    PageDescrJekyll(rel_path=PosixPath('subdir/page.md'), is_root=False, is_index=False, is_fragment=False, main_url='/subdir/page.html', all_urls=['/subdir/page.html', '/subdir/page'], builtin_redirects=[])
    """
    if list(rel_path.parents)[-2:] == [pathlib.Path("_includes"), pathlib.Path(".")]:
        return PageDescrJekyll(
            rel_path=rel_path,
            is_index=False,
            is_root=False,
            is_fragment=True,
        )
    is_root = rel_path.parent == pathlib.Path(".")
    is_index = rel_path.name == "index.md"
    main_url = f"/{rel_path.with_suffix(".html")}"
    all_urls = [main_url, f"/{rel_path.with_suffix("")}"]
    builtin_redirects = []
    if is_root and is_index:
        main_url = "/"
        all_urls += ["/"]
    elif is_index:
        main_url = f"/{rel_path.parent}/"
        all_urls.append(main_url)
        builtin_redirects = [f"/{rel_path.parent}"]
    return PageDescrJekyll(
        rel_path=rel_path,
        is_index=is_index,
        is_root=is_root,
        is_fragment=False,
        main_url=main_url,
        all_urls=all_urls,
        builtin_redirects=builtin_redirects,
    )


def convert_page_descr(src: PageDescrJekyll, path_mappings: dict[str, str]) -> PageDescrMint:
    """Convert a Jekyll page description to a Mint page description.
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("index.md")), {"index.md": "index.mdx"})
    PageDescrMint(rel_path=PosixPath('index.mdx'), is_root=True, is_index=True, is_fragment=False, main_url='/')
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("Dir/index.md")), {"Dir": "dir"})
    PageDescrMint(rel_path=PosixPath('dir.mdx'), is_root=False, is_index=True, is_fragment=False, main_url='/dir')
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("Dir/page.md")), {"Dir": "dir"})
    PageDescrMint(rel_path=PosixPath('dir/page.mdx'), is_root=False, is_index=False, is_fragment=False, main_url='/dir/page')
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("Dir/index.md")), {"Dir": "dir/subdir"})
    PageDescrMint(rel_path=PosixPath('dir/subdir.mdx'), is_root=False, is_index=True, is_fragment=False, main_url='/dir/subdir')
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("Dir/page.md")), {"Dir": "dir/subdir"})
    PageDescrMint(rel_path=PosixPath('dir/subdir/page.mdx'), is_root=False, is_index=False, is_fragment=False, main_url='/dir/subdir/page')
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("Dir/subdir/index.md")), {"Dir": "dir"})
    PageDescrMint(rel_path=PosixPath('dir/subdir.mdx'), is_root=False, is_index=True, is_fragment=False, main_url='/dir/subdir')
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("Dir/subdir/page.md")), {"Dir": "dir"})
    PageDescrMint(rel_path=PosixPath('dir/subdir/page.mdx'), is_root=False, is_index=False, is_fragment=False, main_url='/dir/subdir/page')
    >>> convert_page_descr(build_page_descr_jekyll(pathlib.Path("Overview/Security/security.md")),
    ...     {"Overview": "overview", "Overview/security": "overview/security", "Overview/Security/security.md": "overview/security/index.mdx"})
    PageDescrMint(rel_path=PosixPath('overview/security.mdx'), is_root=False, is_index=True, is_fragment=False, main_url='/overview/security')
    """
    rel_path: pathlib.Path | None = None
    if str(src.rel_path) in path_mappings:
        rel_path = pathlib.Path(path_mappings[str(src.rel_path)])
    else:
        for path in src.rel_path.parents:
            if str(path) in path_mappings:
                rel_path = (pathlib.Path(path_mappings[str(path)]) / src.rel_path.relative_to(path)).with_suffix(".mdx")
                break
    if rel_path is None:
        raise Exception(f"no mapping found for {src.rel_path}")
    is_index = rel_path.name == "index.mdx"
    is_root = is_index and rel_path.parent == pathlib.Path(".")
    if is_index and not is_root:
        rel_path = rel_path.parent.with_suffix(".mdx")
    if not rel_path.name.endswith(".mdx"):
        raise Exception(f"invalid path mapping for {src.rel_path}: {rel_path}")
    if re.search(r'[\sA-Z]', str(rel_path)):
        raise Exception(f"invalid path mapping for {src.rel_path}: {rel_path} contains upper-case or whitespace characters")
    main_url = f"/{rel_path.with_suffix('')}" if not src.is_fragment else None
    if is_root:
        main_url = "/"
    return PageDescrMint(
        rel_path=rel_path,
        is_root=is_root,
        is_index=is_index,
        is_fragment=src.is_fragment,
        main_url=main_url,
    )


def parse_page_jekyll(page: str, descr: PageDescrJekyll) -> PageJekyll:
    """Parse a page from a string.
    >>> parse_page_jekyll('# Header\\nContent', build_page_descr_jekyll(pathlib.Path("_includes/page.md"))).content
    '# Header\\nContent'
    >>> parse_page_jekyll('---\\ntitle: bar\\n---\\n# Header\\nContent', build_page_descr_jekyll(pathlib.Path("page.md"))).content
    '# Header\\nContent'
    >>> utils.filter_none(dataclasses.asdict(parse_page_jekyll('---\\ntitle: bar\\n---\\n# Header\\nContent', build_page_descr_jekyll(pathlib.Path("page.md"))).fm))
    {'title': 'bar'}
    >>> parse_page_jekyll('---\\n---\\n# Header\\nContent', build_page_descr_jekyll(pathlib.Path("page.md"))).content
    '# Header\\nContent'
    >>> utils.filter_none(dataclasses.asdict(parse_page_jekyll('---\\n---\\n# Header\\nContent', build_page_descr_jekyll(pathlib.Path("page.md"))).fm))
    {}
    """
    if descr.is_fragment:
        return PageJekyll(
            descr=descr,
            fm=None,
            content=page
        )
    frontmatter_match = re.match(r'^---\n(.*?)---\n', page, re.DOTALL)
    if frontmatter_match is None:
        raise Exception(f"front matter not found")
    fm = frontmatter_match.group(0)
    fm_yaml = frontmatter_match.group(1)
    fm_raw = yaml.safe_load(fm_yaml) or {}
    return PageJekyll(
        descr=descr,
        fm=FrontMatterJekyll(**fm_raw),
        content=page[len(fm):]
    )


def render_page_mint(p: PageMint) -> str:
    if p.descr.is_fragment:
        return p.content
    fm_dict = utils.filter_none(dataclasses.asdict(p.fm))
    fm_raw = yaml.dump(fm_dict, default_flow_style=False)
    return f"---\n{fm_raw}---\n{p.content}\n"
