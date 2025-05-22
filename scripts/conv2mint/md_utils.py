import difflib
from dataclasses import dataclass

import markdown_it as md
import markdown_it.parser_block as md_b
import markdown_it.parser_core as md_c


@dataclass(kw_only=True)
class Block:
    tokens: list[tuple[int, md_b.Token]]
    content: str

    def is_empty(self) -> bool:
        return self.content == "" and not self.tokens

    def get_types(self) -> list[str]:
        return [t[1].type for t in self.tokens]

    def is_inline(self) -> bool:
        return "inline" in self.get_types()

    def is_html_block(self) -> bool:
        return "html_block" in self.get_types()

    def is_fence(self) -> bool:
        return "fence" in self.get_types()

    def get_header(self) -> md_b.Token | None:
        for t in self.tokens:
            if t[1].type == "heading_open":
                return t[1]
        return None


def split_into_blocks(src: str) -> list[Block]:
    """
    Splits a markdown string into blocks, each containing a segment of content and the list of tokens which map to that segment.
    The segments are non-overlapping and are covering the entire content.
    >>> [([t.type for _, t in b.tokens], b.content) for b in split_into_blocks("")]
    []
    >>> [([t.type for _, t in b.tokens], b.content) for b in split_into_blocks("a\\n\\n\\n\\nc\\n\\n")]
    [(['paragraph_open', 'inline'], 'a\\n'), ([], '\\n\\n\\n'), (['paragraph_open', 'inline'], 'c\\n'), ([], '\\n')]
    """
    mit = md.MarkdownIt()
    sc = md_c.StateCore(src, mit, {})
    md_c.normalize(sc)
    src = sc.src
    state = md_b.StateBlock(src, mit, {}, [])
    mit.block.tokenize(state, state.line, state.lineMax)

    lines = []
    for m in zip(state.bMarks, state.eMarks):
        lines.append(state.src[m[0]:m[1] + 1])

    line_tokens = []
    for i in range(len(lines)):
        line_tokens.append([])

    for i, t in enumerate(state.tokens):
        if t.map is not None:
            for j in range(t.map[0], t.map[1]):
                line_tokens[j].append(i)

    res = []
    last_start = 0
    last_tokens = []
    for i, line_tokens in enumerate(line_tokens):
        if last_tokens != line_tokens:
            if i > 0:
                b = Block(tokens=[(x, state.tokens[x]) for x in last_tokens], content="".join(lines[last_start:i]))
                if not b.is_empty():
                    res.append(b)
            last_start = i
            last_tokens = line_tokens
    b = Block(tokens=[(x, state.tokens[x]) for x in last_tokens], content="".join(lines[last_start:]))
    if not b.is_empty():
        res.append(b)
    return res


def join_blocks(blocks: list[Block]) -> str:
    """
    Unsplits a list of blocks into a single string.
    >>> join_blocks([Block(tokens=[], content="a\\n"), Block(tokens=[], content="\\n\\n\\n"), Block(tokens=[], content="c\\n")])
    'a\\n\\n\\n\\nc\\n'
    """
    return "".join([b.content for b in blocks])


def compare_block_metadata(
        blocks_old: list[Block],
        blocks_new: list[Block],
        equivalent_block_meta: list[tuple[list[str], list[str]]] | None
) -> tuple[list[str], list[str], list[str]] | None:
    """
    A utility function to validate that the high-level layout of the markdown content stays the same.
    Compares the metadata of two lists of blocks and returns the differences between the metadata,
    and auxiliary diff which includes the content.
    >>> compare_block_metadata(
    ...     [Block(tokens=[(0, md_b.Token(type="paragraph_open", tag="p", nesting=1)), (1, md_b.Token(type="inline", tag='', nesting=0))], content="a\\n")],
    ...     [Block(tokens=[(0, md_b.Token(type="html_block", tag="", nesting=0))], content="<div>a</div>\\n")],
    ...     equivalent_block_meta=[(["html_block"], ["paragraph_open", "inline"])]) is None
    True
    >>> compare_block_metadata(     # doctest: +NORMALIZE_WHITESPACE
    ...     [Block(tokens=[(0, md_b.Token(type="paragraph_open", tag="p", nesting=1)), (1, md_b.Token(type="inline", tag='', nesting=0))], content="a\\n")],
    ...     [Block(tokens=[(0, md_b.Token(type="paragraph_open", tag="p", nesting=1)), (1, md_b.Token(type="inline", tag='', nesting=0))], content="# a\\n")],
    ...     equivalent_block_meta=None)
    (['--- meta_old\\n', '+++ meta_new\\n', '@@ -1 +1 @@\\n',
      '-B: paragraph_open/inline', '+B: heading_open/inline'],
     ['--- meta_content_old\\n', '+++ meta_content_new\\n',
      '@@ -1 +1 @@\\n',
      "-B: paragraph_open/inline :: 'a\\\\n'",
      "+B: heading_open/inline :: '# a\\\\n'"],
     ['--- content_old\\n', '+++ content_new\\n',
      '@@ -1 +1 @@\\n',
      '-a\\n',
      '+# a\\n'])
    """
    equivalent_block_meta = equivalent_block_meta or []
    meta_old = _render_block_metadata(_normalize_block_metadata(_get_block_metadata(blocks_old), equivalent_block_meta))
    blocks_reparsed_new = split_into_blocks(join_blocks(blocks_new))
    meta_new = _render_block_metadata(_normalize_block_metadata(_get_block_metadata(blocks_reparsed_new), equivalent_block_meta))
    meta_diff = list(difflib.unified_diff(meta_old, meta_new, "meta_old", "meta_new"))
    if not meta_diff:
        return None
    meta_content_old = _render_block_metadata_with_content(blocks_old)
    meta_content_new = _render_block_metadata_with_content(blocks_reparsed_new)
    meta_content_diff = list(difflib.unified_diff(meta_content_old, meta_content_new, "meta_content_old", "meta_content_new"))
    content_old = join_blocks(blocks_old)
    content_new = join_blocks(blocks_new)
    content_diff = list(difflib.unified_diff(content_old.splitlines(keepends=True), content_new.splitlines(keepends=True), "content_old", "content_new"))
    return meta_diff, meta_content_diff, content_diff


def _get_block_metadata(blocks: list[Block]) -> list[list[str]]:
    """
    Renders the metadata of a list of blocks.
    >>> _get_block_metadata([
    ...     Block(tokens=[(0, md_b.Token(type="foo", tag="foo", nesting=1)), (1, md_b.Token(type="bar", tag="bar", nesting=0))], content="a\\n"),
    ...     Block(tokens=[], content="\\n"),
    ...     Block(tokens=[(2, md_b.Token(type="foo", tag="foo", nesting=1))], content="b\\n")])
    [['foo', 'bar'], [], ['foo']]
    """
    return [b.get_types() for b in blocks]


def _normalize_block_metadata(block_meta: list[list[str]], equivalent_blocks: list[tuple[list[str], list[str]]]) -> list[list[str]]:
    """Conflates equivalent block metadata.
    >>> _normalize_block_metadata([["a", "b", "c", "d"], ["a", "b", "c"], ["b", "c"], ["b"], ["c"], []], [(["b", "c"], ["e"])])
    [['a', 'e', 'd'], ['a', 'e'], ['e'], ['b'], ['c'], []]
    """
    def render(m: list[str]) -> str:
        if not m:
            return "/"
        return f"/{'/'.join(m)}/"

    eq = {}
    for k, v in equivalent_blocks:
        eq[render(k)] = render(v)

    res = []
    for b in block_meta:
        b_str = render(b)
        for k in eq:
            b_str = b_str.replace(k, eq[k])
        b_str = b_str.strip("/")
        if b_str == "":
            res.append([])
            continue
        res.append(b_str.split("/"))
    return res


def _render_block_metadata(block_meta: list[list[str]]) -> list[str]:
    """
    Renders the metadata of a list of blocks.
    >>> _render_block_metadata([["foo", "bar"], [], ["foo"]])
    ['B: foo/bar', 'B: ', 'B: foo']
    """
    return [f"B: {"/".join(b)}" for b in block_meta]


def _render_block_metadata_with_content(blocks: list[Block]) -> list[str]:
    """
    Renders the metadata of a list of blocks with content.
    >>> _render_block_metadata_with_content([
    ...     Block(tokens=[(0, md_b.Token(type="foo", tag="foo", nesting=1)), (1, md_b.Token(type="bar", tag="bar", nesting=0))], content="a\\n"),
    ...     Block(tokens=[], content="\\n"),
    ...     Block(tokens=[(2, md_b.Token(type="foo", tag="foo", nesting=1))], content="b\\n")])
    ["B: foo/bar :: 'a\\\\n'", "B:  :: '\\\\n'", "B: foo :: 'b\\\\n'"]
    """
    return [f"B: {"/".join(b.get_types())} :: {b.content!r}" for b in blocks]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
