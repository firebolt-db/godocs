import dataclasses
import pprint

import page


@dataclasses.dataclass(kw_only=True)
class Group:
    index: page.ParsedPage | None
    children: list['Group']


def rebuild_navigation(pages: list[page.ParsedPage]) -> Group:
    title2pages: dict[str, dict[str, str]] = {}
    page2group: dict[str, Group] = {}
    for p in pages:
        if not p.fm.title:
            raise Exception(f"page {p.rel_path} has no title")
        page2group[str(p.rel_path)] = Group(index=p, children=[])
        title2pages.setdefault(p.fm.title, {})[p.fm.parent or ""] = str(p.rel_path)

    root_g = Group(index=None, children=[])
    title2pages[""] = {"": ""}
    page2group[""] = root_g

    def get_group(title: str | None, parent: str | None) -> Group | None:
        title = title or ""
        parent = parent or ""
        gs = title2pages.get(title, {})
        if len(gs) == 1:
            return page2group[list(gs.values())[0]]
        return page2group.get(gs.get(parent))

    pprint.pprint({k: v for k, v in title2pages.items() if len(v) > 1})
    for p in pages:
        self_g = get_group(p.fm.title, p.fm.parent)
        if self_g is None:
            raise Exception(f"page {p.rel_path} has no group")
        parent_g = get_group(p.fm.parent, p.fm.grand_parent)
        if parent_g is None:
            raise Exception(f"page {p.rel_path} has no parent group")
        parent_g.children.append(self_g)

    return root_g

#
#
#
# def generate_navigation(root: Group) -> dict[str, dict[]]:

def print_navigation(root: Group, level: int = 0) -> None:
    title = root.index.fm.title if root.index else "ROOT"
    rel_path = root.index.rel_path if root.index else ""
    print("  " * level + f"[{title}]({rel_path})")
    for child in root.children:
        print_navigation(child, level + 1)
