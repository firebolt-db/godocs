import json
import pathlib
import re
import sys


def main(regenerate: bool) -> None:
    root_dir = pathlib.Path(__file__).parent.parent
    docs_dir = root_dir / "docs-mdx"
    docs_json = json.loads((docs_dir / 'docs.json').read_text())
    known_pages = set(json.loads((root_dir / "known_pages.json").read_text()))

    slugs = set()
    redirect_pages = set()
    for r in docs_json.get("redirects", []):
        if re.match("^.*?/:\\w+[*]", r["source"]):
            src = re.sub("^(.*/):\\w+[*]", r"\1(.*)", r["source"])
            slugs.add(src)
        else:
            redirect_pages.add(r["source"])

    existing_pages = set()
    for page_path in docs_dir.glob("**/*.mdx"):
        rel_page_path = page_path.relative_to(docs_dir)
        if str(rel_page_path).startswith("snippets/"):
            continue
        page = f'/{str(rel_page_path).removesuffix(".mdx").removeprefix("./")}'
        existing_pages.add(page)
        redirect_pages.add(f"{page}/")

    for page in sorted(known_pages):
        if page not in existing_pages and page not in redirect_pages and not any(re.match(src, page) for src in slugs):
            raise ValueError(f"Page {page} is a previously known page but is no longer found in existing pages or redirects. Consider adding a redirect for it or removing it from known_pages.json")

    new_known_pages = known_pages | existing_pages | redirect_pages
    if new_known_pages != known_pages:
        if regenerate:
            (root_dir / "known_pages.json").write_text(json.dumps(sorted(new_known_pages), indent=2))
        else:
            raise ValueError(
                "The known pages list is out of date. "
                "Run the script with 'regenerate' argument to update it."
            )


if __name__ == "__main__":
    main(len(sys.argv) > 1 and sys.argv[1] == "regenerate")
