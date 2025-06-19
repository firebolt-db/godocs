#!/usr/bin/env python3
import json
import pathlib
import re


def check_redirect_loops(all_pages: list, redirects: list) -> None:
    # built-in redirects
    for p in all_pages:
        redirects.append({
            "source": f"{p}/",
            "destination": f"{p}"
        })

    slug_edges = {}
    # slug redirects
    for r in redirects:
        if re.match("^.*?/:\\w+[*]", r["source"]):
            src = re.sub("^(.*/):\\w+[*]", r"\1(.*)", r["source"])
            dst = re.sub("^(.*/):\\w+[*]", r"\1\\1", r["destination"])
            if not slug_edges.get(src):
                slug_edges[src] = dst
            elif slug_edges[src] != dst:
                raise ValueError(f"Slug redirects for {src} are not consistent: {slug_edges[src]} vs {dst}")

    edges = {}
    for r in redirects:
        src, dst = r["source"], r["destination"]
        if not edges.get(src):
            edges[src] = dst
        elif edges[src] != dst:
            raise ValueError(f"Redirects for {src} are not consistent: {edges[src]} vs {dst}")

    for p in all_pages:
        if p in edges:
            raise ValueError(f"{p} is both a page and a redirect to {edges[p]}. !!!! Be careful with exiting redirects. They may get cached by browsers or search engines. If a new page is created with the same URL as a cached redirect, that page would be inaccessible !!!!")
        for src, dst in slug_edges.items():
            if re.match(src, p):
                raise ValueError(f"{p} matches slug redirect {src} -> {dst}, which is not allowed")

    for n in sorted(edges.keys()):
        visited = set()
        path = []
        q = [n]
        while q:
            u = q.pop()
            visited.add(u)
            path.append(u)
            v = edges.get(u)
            if v:
                if v in visited:
                    raise ValueError(f"Loop detected in redirects for {n}: {" -> ".join(path)} -> {v}")
                q.append(v)
            for src, dst in slug_edges.items():
                if re.match(src, u):
                    v = re.sub(src, dst, u)
                    if v in visited:
                        raise ValueError(f"Loop detected in slug redirects for {n}: {" -> ".join(path)} -> {v}")
                    q.append(v)


def main():
    root_dir = pathlib.Path(__file__).parent.parent
    docs_dir = root_dir / "docs-mdx"
    docs_json = json.loads((docs_dir / 'docs.json').read_text())

    all_pages = [f'/{str(p.relative_to(docs_dir)).removesuffix(".mdx").removeprefix("./")}' for p in docs_dir.glob("**/*.mdx")]
    check_redirect_loops(all_pages, docs_json["redirects"])


if __name__ == "__main__":
    main()
