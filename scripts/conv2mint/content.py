import pathlib
import re
import typing

import markdown_it.parser_block as md_b

import markdown
import page


class MarkdownStructureChangedException(Exception):
    meta_diff: list[str]
    meta_content_diff: list[str]
    content_diff: list[str]
    blocks_old: list[markdown.Block]
    blocks_new: list[markdown.Block]

    def __init__(self, meta_diff: list[str], meta_content_diff: list[str], content_diff: list[str],
                 blocks_old: list[markdown.Block], blocks_new: list[markdown.Block],
                 message: str = "Markdown structure changed"):
        super().__init__(message)
        self.meta_diff = meta_diff
        self.meta_content_diff = meta_content_diff
        self.content_diff = content_diff
        self.blocks_old = blocks_old
        self.blocks_new = blocks_new

    def __str__(self) -> str:
        m = "\n".join(self.meta_diff)
        mc = "\n".join(self.meta_content_diff)
        c = "".join(self.content_diff)
        return f"{str(super())}\n===== meta diff:\n{m}\n==== meta and content diff:\n{mc}\n==== content diff:\n{c}"


def convert_page(src: page.PageJekyll, descr: page.PageDescrMint, url_mapping: dict[str, str]) -> page.PageMint:
    return page.PageMint(
        descr=descr,
        fm=_convert_front_matter(src.fm, descr) if src.fm else None,
        content=_convert_markdown_content(src.content, src.descr, url_mapping),
    )


def _convert_front_matter(
        fm: page.FrontMatterJekyll,
        dst_descr: page.PageDescrMint,
) -> page.FrontMatterMint:
    return page.FrontMatterMint(
        title=fm.title,
        description=fm.description,
        sidebarTitle=("Overview" if dst_descr.is_index and not dst_descr.is_root else fm.title),
        groups=([] if fm.published is False else None),
        # mode="wide",
    )


def _convert_markdown_content(content: str, descr: page.PageDescrJekyll, url_mapping: dict[str, str]) -> str:
    # Keeping the original blocks aside to revalidate the markup later
    # to ensure it's not mingled by the transformations
    blocks_orig = markdown.split_into_blocks(content)
    # Same result, independent copy
    blocks = markdown.split_into_blocks(content)
    blocks = _transform_content(blocks, _normalize_html_tags_in_content)
    blocks = _transform_content(blocks, _strip_html_comments)
    # Strip file type extensions from links
    blocks = _transform_content(blocks, _convert_link_tags)
    # todo: merge into _convert_page_urls
    blocks = _transform_content(blocks, _convert_asset_urls)
    blocks = _transform_content(blocks, lambda s: _convert_page_urls(s, descr, url_mapping))
    blocks = _transform_content(blocks, _convert_jtd_image_attrs)
    blocks = _transform_content(blocks, _strip_jtd_link_attrs)
    # # TODO: fix includes
    blocks = _transform_content(blocks, _strip_include_tags)
    blocks = _transform_content(blocks, _convert_jtd_block_attrs)

    # The operations above shouldn't change the _Block-level parsing
    # if diff := markdown.compare_block_metadata(blocks_orig, blocks, [(["html_block"], ["paragraph_open", "inline"])]):
    #     raise MarkdownStructureChangedException(diff[0], diff[1], diff[2], blocks_orig, blocks)

    blocks = _transform_content(blocks, _strip_toc_markers)
    blocks = _transform_content(blocks, _strip_jtd_attrs)
    blocks = _convert_h1(blocks)
    for b in blocks:
        if b.is_inline() or b.is_html_block():
            _check_unconverted(b)
    return markdown.join_blocks(blocks)


def _transform_content(blocks: list[markdown.Block], func: typing.Callable[[str], str]) -> list[markdown.Block]:
    res = []
    for b in blocks:
        if b.is_inline() or b.is_html_block():
            res.append(markdown.Block(tokens=b.tokens, content=func(b.content)))
        else:
            res.append(b)
    return res


def _normalize_html_tags_in_content(content: str) -> str:
    """Normalizes HTML tags in the content.
    >>> _normalize_html_tags_in_content('<BR>Some content<br>More content')
    '<br/>Some content<br/>More content'
    >>> _normalize_html_tags_in_content('<HR>Some content<hr>More content')
    '<hr/>Some content<hr/>More content'
    >>> _normalize_html_tags_in_content('<IMG src="image.png">Some content<img src="image.png" />More content')
    '<img src="image.png"/>Some content<img src="image.png"/>More content'
    """
    content = re.sub(r'<br\s*/?>', '<br/>', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<hr\s*/?>', '<hr/>', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<img(\s.*?)\s*/?>', r'<img\1/>', content, flags=re.IGNORECASE | re.DOTALL)
    return content


def _convert_asset_urls(content: str) -> str:
    """Convert asset paths from Jekyll to Mintlify format.
    >>> _convert_asset_urls('![alt text](.././../assets/image.png)')
    '![alt text](/assets/image.png)'
    >>> _convert_asset_urls('![alt text](..//.//..//assets/image.png)')
    '![alt text](/assets/image.png)'
    >>> _convert_asset_urls('![alt text](//assets/image.png)')
    '![alt text](/assets/image.png)'
    >>> _convert_asset_urls('![alt text](/assets/image.png)')
    '![alt text](/assets/image.png)'
    >>> _convert_asset_urls('<img src="../assets/image.png" />')
    '<img src="/assets/image.png" />'
    """
    return re.sub(r'(?:\.\.?/+|/+)*assets/', '/assets/', content)


def _convert_page_urls(content: str, descr: page.PageDescrJekyll, url_mapping: dict[str, str]) -> str:
    """Strips .md and .html from internal links.
    >>> _convert_page_urls('[Link](path/to/file.md)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/dir/path/to/file.md": '/other/path/to/file'})
    '[Link](/other/path/to/file)'
    >>> _convert_page_urls('<a href="path/to/file.md">Link</a>', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/dir/path/to/file.md": '/other/path/to/file'})
    '<a href="/other/path/to/file">Link</a>'
    >>> _convert_page_urls('<img src="../assets/to/file.png" alt="Pic"/>', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/dir/path/to/file.md": '/other/path/to/file'})
    '<img src="/assets/to/file.png" alt="Pic"/>'
    >>> _convert_page_urls('[Link](path/to/file.md#frag)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/dir/path/to/file.md": '/other/path/to/file'})
    '[Link](/other/path/to/file#frag)'
    >>> _convert_page_urls('[Link](index.md)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/dir/index.md": '/other'})
    '[Link](/other)'
    >>> _convert_page_urls('[Link](index.md)', page.build_page_descr_jekyll(pathlib.Path('other.md')), url_mapping={"/index.md": '/'})
    '[Link](/)'
    >>> _convert_page_urls('[Link](index.md)', page.build_page_descr_jekyll(pathlib.Path('index.md')), url_mapping={"/index.md": '/'})
    '[Link](/)'
    >>> _convert_page_urls('[Link](index.md#frag)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/dir/index.md": '/other'})
    '[Link](/other#frag)'
    >>> _convert_page_urls('[Link](index.md#frag)', page.build_page_descr_jekyll(pathlib.Path('other.md')), url_mapping={"/index.md": '/'})
    '[Link](/#frag)'
    >>> _convert_page_urls('[Link](index.md#frag)', page.build_page_descr_jekyll(pathlib.Path('index.md')), url_mapping={"/index.md": '/'})
    '[Link](/#frag)'
    >>> _convert_page_urls('[Link](../path/to/file.md) [Link](../path/to/file.md)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/path/to/file.md": '/other/to/file'})
    '[Link](/other/to/file) [Link](/other/to/file)'
    >>> _convert_page_urls('[Link](../path/to/file.html)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/path/to/file.html": '/other/to/file'})
    '[Link](/other/to/file)'
    >>> _convert_page_urls('[Link](../path/to/file)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/path/to/file": '/other/to/file'})
    '[Link](/other/to/file)'
    >>> _convert_page_urls('[Link](#anchor)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={})
    '[Link](#anchor)'
    >>> _convert_page_urls('[Link]()', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={})
    '[Link](#)'
    >>> _convert_page_urls('[Link](../path/to/file.md#anchor)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/path/to/file.md": '/other/to/file'})
    '[Link](/other/to/file#anchor)'
    >>> _convert_page_urls('[Link](../path/to/file.html#anchor)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/path/to/file.html": '/other/to/file'})
    '[Link](/other/to/file#anchor)'
    >>> _convert_page_urls('[Link](../path/to/file#anchor)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/path/to/file": '/other/to/file'})
    '[Link](/other/to/file#anchor)'
    >>> _convert_page_urls('[Link](https://example.com/path/to/file.md)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={})
    '[Link](https://example.com/path/to/file.md)'
    >>> _convert_page_urls('[Link](git+ssh:example.com/path/to/file.md)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={})
    '[Link](git+ssh:example.com/path/to/file.md)'
    >>> _convert_page_urls('[Link](mail:a@b.md)', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={})
    '[Link](mail:a@b.md)'
    >>> _convert_page_urls('    * **Database** - A logical collection of schemas and data objects, such as tables and views, that organizes and manages user data and metadata for querying and data processing. For more information about databases see [Create a Database](/Guides/getting-started/get-started-sql.md#create-a-database) in the [Get started using SQL](/Guides/getting-started/get-started-sql.md) guide. Under database are the following levels:\\n', page.build_page_descr_jekyll(pathlib.Path('dir/other.md')), url_mapping={"/Guides/getting-started/get-started-sql.md": '/guides/getting-started/get-started-sql'})
    '    * **Database** - A logical collection of schemas and data objects, such as tables and views, that organizes and manages user data and metadata for querying and data processing. For more information about databases see [Create a Database](/guides/getting-started/get-started-sql#create-a-database) in the [Get started using SQL](/guides/getting-started/get-started-sql) guide. Under database are the following levels:\\n'
    """
    def fix_url(url: str) -> str:
        if re.match(r'^[a-z][a-z0-9+.-]*:', url, flags=re.IGNORECASE) is not None:
            # external link
            return url
        url, frag = url.split('#', 1) if '#' in url else (url, '')
        if not url:
            return f"#{frag}"
        abs_url = pathlib.Path(url)
        if not abs_url.is_absolute():
            abs_url = (pathlib.Path("/") / descr.rel_path.parent / pathlib.Path(url)).resolve()
        if str(abs_url) in url_mapping:
            abs_url = url_mapping[str(abs_url)]
        elif abs_url.name.endswith(".md") or abs_url.name.endswith(".html"):
            raise Exception(f"can't find url {abs_url} in url_mapping")
        return str(abs_url) + ('#' + frag if frag else '')

    content = re.sub(r'\[(.*?)\]\((.*?)\)',
                     lambda x: f"[{x.group(1)}]({fix_url(x.group(2))})", content)
    content = re.sub(r'\b(href|src)="(.*?)"',
                     lambda x: f'{x.group(1)}="{fix_url(x.group(2))}"', content)
    return content


def _convert_link_tags(content: str) -> str:
    """Convert {% link path %} links to /path.
    >>> _convert_link_tags('Some content [a link]({% link path %})')
    'Some content [a link](/path)'
    """
    return re.sub(r'\{%\s*link\s+([^}]+)\s+%\}', r'/\1', content, flags=re.DOTALL)


def _convert_jtd_image_attrs(content: str) -> str:
    """Convert Jekyll image attributes to Mintlify format.
    >>> _convert_jtd_image_attrs('![alt text](image.png){: width="50%" .centered}')
    '<img src="image.png" alt="alt text" width="50%"/>'
    >>> _convert_jtd_image_attrs('![alt text](image.png){:width="50%"}')
    '<img src="image.png" alt="alt text" width="50%"/>'
    >>> _convert_jtd_image_attrs('![alt text](image.png)')
    '![alt text](image.png)'
    """
    def convert_img(match: re.Match) -> str:
        alt_text = match.group(1)
        src = match.group(2)
        # .centered attribute did not work in original documentation, no point in keeping it
        attrs = re.sub(r'\s*\.centered\b', '', match.group(3), flags=re.DOTALL).strip()
        return f'<img src="{src}" alt="{alt_text}" {attrs}/>'
    return re.sub(r'!\[(.*?)\]\((.*?)\)\{:(.*?)\}', convert_img, content, flags=re.DOTALL)


def _strip_jtd_link_attrs(content: str) -> str:
    """Remove Jekyll attributes from markdown links.
    >>> _strip_jtd_link_attrs('[Link](path/to/file){:target="_blank"}')
    '[Link](path/to/file)'
    >>> _strip_jtd_link_attrs('[Link](path/to/file)')
    '[Link](path/to/file)'
    """
    return re.sub(r'(\[.*?\]\(.*?\))\{:.*?\}', r'\1', content)


def _strip_include_tags(content: str) -> str:
    """Strips Jekyll include tags from markdown content if present.
    >>> _strip_include_tags('{% include path/to/file.md %}')
    '**INCLUDE WAS HERE**'
    >>> _strip_include_tags('Some content {% include path/to/file.md %} More content')
    'Some content **INCLUDE WAS HERE** More content'
    >>> _strip_include_tags('No % include tag % here')
    'No % include tag % here'
    """
    return re.sub(r'\{%\s*include\s+.*?%\}', '**INCLUDE WAS HERE**', content, flags=re.DOTALL)


def _strip_html_comments(content: str) -> str:
    """Strips HTML comments from markdown content if present.
    >>> _strip_html_comments('Some content <!-- Comment --> More content')
    'Some content  More content'
    >>> _strip_html_comments('Before <!-- Hi<!--By-- -> --> After')
    'Before  After'
    """
    return re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)


def _convert_jtd_block_attrs(content: str) -> str:
    """Convert Jekyll _Block attributes to Mintlify format.
    >>> _convert_jtd_block_attrs("  A paragraph\\n  {:.note}\\n")
    '  <Note>\\n  A paragraph\\n  </Note>\\n'
    >>> _convert_jtd_block_attrs("> A paragraph\\n{:.note}\\n")
    '<Note>\\n> A paragraph\\n</Note>\\n'
    >>> _convert_jtd_block_attrs("  A paragraph\\n  {:.warning}\\n")
    '  <Warning>\\n  A paragraph\\n  </Warning>\\n'
    """
    def transform(m: re.Match) -> str:
        s_1, b_2, s_3, a_4, s_5 = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
        tag = a_4.capitalize()
        return f"{s_1}<{tag}>\n{s_1}{b_2}{s_3}</{tag}>{s_5}"

    return re.sub(r'^(\s*)(.*?)(\s*)\{:\s*\.(note|warning)\s*\}(\s*)$', transform, content, flags=re.DOTALL)


def _convert_h1(blocks: list[markdown.Block]) -> list[markdown.Block]:
    """Deletes first h1 from markdown content if present, demotes all other h1 to h2.
    >>> markdown.join_blocks(_convert_h1([
    ...     markdown.Block(tokens=[],
    ...         content="\\n\\n"),
    ...     markdown.Block(tokens=[
    ...         (0, md_b.Token(type="heading_open", tag="h1", nesting=1, markup='#')),
    ...         (1, md_b.Token(type="paragraph_open", tag='', nesting=1)),
    ...         (2, md_b.Token(type="inline", tag='', nesting=0))],
    ...         content="# Header 1 # something"),
    ...     markdown.Block(tokens=[
    ...         (3, md_b.Token(type="blockquote_open", tag="blockquote", nesting=1)),
    ...         (4, md_b.Token(type="heading_open", tag="h1", nesting=1, markup='#')),
    ...         (5, md_b.Token(type="paragraph_open", tag='', nesting=1)),
    ...         (6, md_b.Token(type="inline", tag='', nesting=0))],
    ...         content="># Header 2 # something"),
    ... ]))
    '\\n\\n>## Header 2 # something'
    """
    headers_cnt = 0
    res = []
    for b in blocks:
        t = b.get_header()
        is_header = t is not None
        is_h1 = is_header and t.tag == "h1"
        is_first_h1 = is_h1 and not headers_cnt
        headers_cnt += is_header
        if is_header and t.markup[0] != '#':
            raise Exception('found alternative header markup')
        if is_first_h1:
            continue
        if is_h1:
            b.content = b.content.replace('# ', '## ', 1)
        res.append(b)
    # fixes all markdown.Block metadata
    return markdown.split_into_blocks(markdown.join_blocks(res))


def _strip_toc_markers(content: str) -> str:
    """Strips Jekyll TOC markers from markdown content if present.
    >>> _strip_toc_markers('* Topic Toc\\n{: toc }\\n')
    ''
    >>> _strip_toc_markers('1. Topic Toc\\n{: toc }\\n')
    ''
    >>> _strip_toc_markers('* Some content\\n1. Other content\\n')
    '* Some content\\n1. Other content\\n'
    """
    content = re.sub(r'\{:\s*.no_toc\s*\}', '', content, flags=re.DOTALL)
    if re.search(r'\{:\s*toc\s*\}', content, flags=re.DOTALL) is not None:
        return ""
    return content


def _strip_jtd_attrs(content: str) -> str:
    """Strips Jekyll attributes from markdown content if present.
    >>> _strip_jtd_attrs('  Some content\\n  {:#id .class}\\nmore content')
    '  Some content\\n  more content'
    >>> _strip_jtd_attrs('  Some content\\n  {: style="color: red"}\\nmore content')
    '  Some content\\n  more content'
    """
    return re.sub(r'^(\s*)\{:.*?\}\s*', r'\1', content, flags=re.MULTILINE)


def _check_unconverted(b: markdown.Block) -> None:
    if b.is_fence():
        return
    # {% %} or {: %} or {{ }}
    if m := re.search(r"\{[%:{].*?\}", b.content):
        raise Exception(f"found unconverted jekyll or jtd markup {m.group(0)}\n{b.get_types()}\n{b.content}")
    if m := re.search(r"\[.*?\]\([./].*?\.(md|html)(#.*?)\)", b.content):
        raise Exception(f"found unconverted url {m.group(0)}\n{b.get_types()}\n{b.content}")
    if m := re.search(r'<a[^>]+?href="[./].*?\.(md|html)(#.*?)"', b.content):
        raise Exception(f"found unconverted url {m.group(0)}\n{b.get_types()}\n{b.content}")
    if not (re.search(r'`.*?\[.*?\]\[.*?\].*?`', b.content)) \
            and (m := re.search(r'\[[^`[]*?\]\[[^`[]*?\]', b.content)):
        raise Exception(f"found unconverted reference link {m.group(0)}\n{b.get_types()}\n{b.content}")
    if m := re.search(r'(\*|1\.|1\)).*?\btoc\b', b.content, flags=re.IGNORECASE):
        raise Exception(f"found unconverted {m.group(0)}\n{b.get_types()}\n{b.content}")
