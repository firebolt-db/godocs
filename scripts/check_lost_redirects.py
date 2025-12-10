import json
import pathlib
import re
import sys


class LostRedirectsError(Exception):
    pass


def check_unmovable_pages(
    docs_dir: pathlib.Path,
    unmovable_pages: list,
) -> None:
    """Check that unmovable pages still exist at their original locations."""
    existing_pages = set()
    for page_path in sorted(docs_dir.glob("**/*.mdx")):
        rel_page_path = page_path.relative_to(docs_dir)
        if str(rel_page_path).startswith("snippets/"):
            continue
        page = f'{str(rel_page_path).removesuffix(".mdx").removeprefix("./")}'
        existing_pages.add(page)

    for page_entry in unmovable_pages:
        if not page_entry.get("path"):
            raise LostRedirectsError(f"Expected an unmovable page with 'path' key, got {page_entry}")
        if not page_entry.get("reason"):
            raise LostRedirectsError(f"Expected an unmovable page with 'reason' key, got {page_entry}")
        
        page_path = page_entry["path"]
        if page_path not in existing_pages:
            raise LostRedirectsError(
                f"Unmovable page '{page_path}' is missing or has been moved. "
                f"Reason: {page_entry['reason']}. "
                f"This page must remain at its original location. "
                f"If you need to move it, first remove it from unmovable_pages.json."
            )


def check_lost_redirects(
    docs_dir: pathlib.Path,
    docs_json: dict,
    known_pages_path: pathlib.Path,
    unmovable_pages: list,
    regenerate: bool,
) -> None:
    check_unmovable_pages(docs_dir, unmovable_pages)
    
    known_pages = set(json.loads(known_pages_path.read_text()))

    slugs = set()
    redirect_pages = set()
    for r in docs_json.get("redirects", []):
        if re.match("^.*?/:\\w+[*]", r["source"]):
            src = re.sub("^(.*/):\\w+[*]", r"\1(.*)", r["source"])
            slugs.add(src)
        else:
            redirect_pages.add(r["source"])

    existing_pages = set()
    for page_path in sorted(docs_dir.glob("**/*.mdx")):
        rel_page_path = page_path.relative_to(docs_dir)
        if str(rel_page_path).startswith("snippets/"):
            continue
        page = f'/{str(rel_page_path).removesuffix(".mdx").removeprefix("./")}'
        existing_pages.add(page)
        redirect_pages.add(f"{page}/")
        if page_path.parent != docs_dir and not page_path.parent.with_suffix(".mdx").exists():
            # if the overview page doesn't exist, Mintlify automatically redirects to one of the group's pages.
            # Marking the overview page as still present as a redirect.
            redirect_pages.add(str(pathlib.Path(page).parent))
            redirect_pages.add(f"{str(pathlib.Path(page).parent)}/")

    for page in sorted(known_pages):
        if page not in existing_pages and page not in redirect_pages and not any(re.match(src, page) for src in slugs):
            raise LostRedirectsError(f"Page {page} is a previously known page but is no longer found in existing pages or redirects. Consider adding a redirect for it or removing it from known_pages.json")

    new_known_pages = known_pages | existing_pages | redirect_pages
    if new_known_pages != known_pages:
        if regenerate:
            known_pages_path.write_text(json.dumps(sorted(new_known_pages), indent=2))
        else:
            raise LostRedirectsError(
                "The known pages list is out of date. "
                "Run the script with 'regenerate' argument to update it. "
                "You can run it by calling 'make' with default target or "
                "specifically 'make check-lost-redirects-regenerate'."
            )


def main(root_dir: pathlib.Path, regenerate: bool) -> None:
    docs_dir = root_dir / "docs-mdx"
    docs_json = json.loads((docs_dir / 'docs.json').read_text())
    known_pages_path = root_dir / "known_pages.json"
    unmovable_pages_path = root_dir / "unmovable_pages.json"
    unmovable_pages = json.loads(unmovable_pages_path.read_text()) if unmovable_pages_path.exists() else []
    check_lost_redirects(docs_dir, docs_json, known_pages_path, unmovable_pages, regenerate)


if __name__ == "__main__":
    main(pathlib.Path(__file__).parent.parent,
         len(sys.argv) > 1 and sys.argv[1] == "regenerate")
