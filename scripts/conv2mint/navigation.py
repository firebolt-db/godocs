import dataclasses
import pathlib
import typing

import page


@dataclasses.dataclass(kw_only=True)
class GroupDescr:
    nav_order: int
    index: page.PageMint
    parent: typing.Optional['GroupDescr'] = None
    children: list['GroupDescr'] = dataclasses.field(default_factory=list)

    def to_json(self) -> str | dict[str, typing.Any]:
        main_url = self.index.descr.main_url.removeprefix('/')
        if not self.index.descr.is_index:
            if len(self.children) > 0:
                raise Exception(f"Group {self.index.descr.main_url} is not an index page but has children")
            return main_url
        if len(self.children) == 0:
            raise Exception(f"Group {self.index.descr.main_url} is an index page but has no children")
        index = [main_url] if not self.index.descr.is_root else []
        return {
            "group": self.index.fm.title,
            "pages": index + [c.to_json() for c in sorted(self.children, key=(lambda c: (c.nav_order, main_url)))],
        }


def build_and_check_url_mapping(pages: list[tuple[page.PageJekyll, page.PageDescrMint]], src_redirects: dict[str, str]) -> dict[str, str]:
    """Validates the page structure ensuring the page structure is regular and consistent:
        - no pages with the same url
        - all directories have an index page of the same name as the directory but with .mdx suffix
        - jtd navigation structure is mapped to the mint directory structure
        - no mint top-level directories are present in jekyll urls including redirects
    """
    src2dst: dict[str, str] = {}
    dst2src: dict[str, str] = {}
    top_dirs: set[str] = set()
    for src_page, dst_descr in pages:
        if src_page.descr.is_fragment:
            continue
        for u in src_page.descr.all_urls + src_page.descr.builtin_redirects:
            src2dst[u] = dst_descr.main_url
        src2dst[f'/{src_page.descr.rel_path}'] = dst_descr.main_url
        if dst_descr.main_url in dst2src:
            raise Exception(f"duplicate destination URL {dst_descr.main_url} for {src_page.descr.main_url} and {dst2src[dst_descr.main_url]}")
        dst2src[dst_descr.main_url] = src_page.descr.main_url
        if dst_descr.is_root:
            continue
        if dst_descr.is_index and (dst_descr.main_url.endswith("/index") or dst_descr.rel_path.name == "index.mdx"):
            raise Exception(f"index page {dst_descr.main_url} hasn't been transformed")
        url_path = pathlib.Path(dst_descr.main_url)
        top_dir = ([dst_descr.main_url] + list(url_path.parents))[-2]
        top_dirs.add(str(top_dir))

    for r in src_redirects:
        r = pathlib.Path(r)
        top_dir = str(([r] + list(r.parents))[-2])
        if top_dir in top_dirs:
            raise Exception(f"redirect {r} is a top-level directory in Mint, which is not allowed")

    return src2dst


def collect_src_redirects(pages: list[page.PageJekyll]) -> dict[str, str]:
    """Collect the preexisting redirects except for the godocs prefix.
    Need to ensure that the redirects in mintlify do not conflict with the old redirects.
    """
    rdr_from_to: dict[str, str] = {}
    for p in pages:
        if p.descr.is_fragment:
            continue
        for r in p.fm.redirect_from or []:
            if r.startswith("/godocs/"):
                continue  # skip godocs redirects
            if r in rdr_from_to and rdr_from_to[r] != p.descr.main_url:
                raise Exception(f"redirect {r} already exists with a different target: {rdr_from_to[r]} != {p.descr.main_url}")
            rdr_from_to[r] = p.descr.main_url
    for p in pages:
        if p.descr.is_fragment:
            continue
        for r in p.descr.builtin_redirects or []:
            if r in rdr_from_to and rdr_from_to[r] != p.descr.main_url:
                print(f"Warning: redirect {r} already exists with a different target: {rdr_from_to[r]} != {p.descr.main_url}")
            rdr_from_to[r] = p.descr.main_url
    return rdr_from_to


def build_navigation_tree(pages: list[tuple[page.PageJekyll, page.PageMint]]) -> GroupDescr:
    """
    Rebuilds the navigation structure from a list of converted pages.
    Returns a dictionary representing the navigation structure.
    """
    url2group = {
        p_mint.descr.main_url: GroupDescr(nav_order=p_jekyll.fm.nav_order or 0, index=p_mint)
        for p_jekyll, p_mint in pages
    }
    for p_jekyll, p_mint in pages:
        print(p_jekyll.descr.main_url, p_mint.descr.main_url)
        if p_mint.descr.is_root:
            continue
        g = url2group[p_mint.descr.main_url]
        if g.parent is not None:
            raise Exception(f"Page {p_mint.descr.main_url} already has a parent: {g.parent.index.descr.main_url}")
        parent = pathlib.Path(p_mint.descr.main_url).parent
        url2group[str(parent)].children.append(g)
    return url2group['/']
