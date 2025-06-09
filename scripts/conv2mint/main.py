import json
import pprint
import shutil
import sys
import pathlib

import page
import content
import navigation


def cleanup_assets(dst_root: pathlib.Path, asset_dirs: list[str]):
    if not dst_root.is_dir() or not dst_root.is_absolute():
        raise Exception(f"Destination root {dst_root} is not a directory or not absolute.")

    for dst in asset_dirs:
        print(f"Removing {dst_root / dst} ...")
        (dst_root / dst).mkdir(parents=True, exist_ok=True)
        shutil.rmtree(dst_root / dst)
        print(f"... done")


def cleanup_pages(dst_root: pathlib.Path, page_descrs: list[page.PageDescrMint]):
    dst_dirs: set[pathlib.Path] = set()
    for descr in page_descrs:
        if len(descr.rel_path.parents) > 1:
            dst_dirs.add(dst_root / descr.rel_path.parents[-2])
        else:
            print(f"Removing {dst_root / descr.rel_path} ...")
            (dst_root / descr.rel_path).unlink(missing_ok=True)
            print(f"... done")

    for d in dst_dirs:
        print(f"Removing directory {d} ...")
        # Ensure that d is not above dst_root
        if not dst_root.is_absolute() or not d.is_absolute() or d == dst_root or not dst_root in d.parents:
            raise Exception(f"Directory {d} is not a subdirectory of {dst_root}")
        d.mkdir(parents=True, exist_ok=True)
        shutil.rmtree(d)
        print(f"... done")


def copy_assets(src_root: pathlib.Path, dst_root: pathlib.Path, asset_globs: list[str], skip_globs: list[str] = None):
    for g in asset_globs:
        print(f"Copying {src_root / g} to {dst_root / g} ...")
        i = 0
        for i, f in enumerate(src_root.glob(g)):
            if skip_globs and any(pathlib.Path(f).match(src_root / skip) for skip in skip_globs):
                print(f"Skipping {f} as it matches skip patterns {skip_globs}")
                continue
            if f.is_file():
                dst_path = dst_root / f.relative_to(src_root)
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(f, dst_path)
        print(f"... done ({i + 1} files copied)")


def main():
    if len(sys.argv) < 3 or "--help" in sys.argv:
        print(f"Usage: {sys.argv[0]} <src_root> <dst_root>")
        return

    src_root, dst_root = pathlib.Path(sys.argv[1]).absolute().resolve(strict=True), pathlib.Path(sys.argv[2]).absolute().resolve(strict=True)

    documentation_top_level_groups = {
        "intro": {"pos": 0, "src": "md"},
        "overview": {"pos": 1, "src": "md"},
        "guides": {"pos": 3, "src": "md"},
        "reference-sql": {"pos": 4, "src": "md"},
        "reference": {"pos": 5, "src": "md"},
        "reference-api": {"pos": 6, "src": "md"},
    }
    firebolt_core_top_level_groups = {
        "firebolt-core": {"pos": 1, "src": "md"},
    }

    # We need to rename all top-level directories because the default platform redirects for directory pages in Jekyll
    #   and Mint are mutually incompatible:
    #   - in Jekyll, it's `/dir` to `/dir/`
    #   - in Mint, it's the other way around: `/dir/` to `/dir`.
    # Browsers cache old redirects, and that would cause infinite redirect loop.
    #
    # We also use this opportunity to fix ugly named directories in the source
    # and ensure the destination directory structure is mapping 1-to-1 to the navigation group structure.
    #
    # NB: Instead of having `dir/index.mdx` we would actually use `dir.mdx`, as mint seems to prefer it over `dir/index.mdx`.
    # But for the sake of consistency and to simplify the conversion, we have 'dir/index.mdx` here.
    # These will translate to `dir.mdx` in the end.
    path_mappings = {
        "index.md":
            "index.mdx",

        "_includes":
            "snippets",

        # have to rename it because it would cause a redirect loop in whoever opened the original page
        "product":
            "intro",

        "Overview":
            "overview",
        "Overview/engine-fundamentals.md":
            "overview/engine-fundamentals/index.mdx",
        "Overview/engine-consumption.md":
            "overview/engine-fundamentals/engine-consumption.mdx",
        "Overview/indexes/using-indexes.md":
            "overview/indexes/index.mdx",
        "Overview/Security":
            "overview/security",
        "Overview/Security/security.md":
            "overview/security/index.mdx",
        "Overview/Security/Role-Based Access Control":
            "overview/security/rbac",

        "Guides":
            "guides",
        "Guides/developing-with-firebolt/connecting-with-Python.md":
            "guides/developing-with-firebolt/connecting-with-python.mdx",
        "Guides/integrations/integrations.md":
            "guides/integrations/index.mdx",
        "Guides/loading-data/loading-data.md":
            "guides/loading-data/index.mdx",
        "Guides/loading-data/working-with-semi-structured-data/working-with-semi-structured-data.md":
            "guides/loading-data/working-with-semi-structured-data/index.mdx",
        "Guides/operate-engines/operate-engines.md":
            "guides/operate-engines/index.mdx",

        "Reference":
            "reference",

        "Reference/release-notes/release-notes.md":
            "reference/release-notes/index.mdx",

        # cannot have sql-reference because it was already used previously and may have conflicting redirects
        "sql_reference":
            "reference-sql",
        "sql_reference/functions-reference/functions-reference.md":
            "reference-sql/functions-reference/index.mdx",
        "sql_reference/functions-reference/JSON":
            "reference-sql/functions-reference/json",
        "sql_reference/functions-reference/Lambda":
            "reference-sql/functions-reference/lambda",

        # for consistency with sql-reference -> reference-sql
        "API-reference":
            "reference-api",
        
        # use consistent naming scheme for firebolt core docs
        "FireboltCore":
            "firebolt-core",
        "FireboltCore/firebolt-core-operation.md":
            "firebolt-core/firebolt-core-operation/index.mdx",
        "FireboltCore/firebolt-core-deployment-compose.md":
            "firebolt-core/firebolt-core-operation/firebolt-core-deployment-compose.mdx",
        "FireboltCore/firebolt-core-deployment-k8s.md":
            "firebolt-core/firebolt-core-operation/firebolt-core-deployment-k8s.mdx",
    }

    pages: list[tuple[page.PageJekyll, page.PageDescrMint]] = []
    for src_f in src_root.rglob('**/*.md'):
        src_descr = page.build_page_descr_jekyll(src_f.relative_to(src_root))
        src_page = page.parse_page_jekyll(src_f.read_text(), src_descr)
        dst_descr = page.convert_page_descr(src_descr, path_mappings)
        pages.append((src_page, dst_descr))

    pages.sort(key=lambda p: p[0].descr.rel_path)

    print(f"Found {len(pages)} pages in source root {src_root}")

    # cleanup_assets(dst_root, [
    #     "assets",
    #     "snippets",
    #     "_includes",
    # ])
    # cleanup_pages(dst_root, [descr for _, descr in pages])
    copy_assets(src_root, dst_root, [
        "assets/**/*",
        "snippets/**/*",
        # "docs.json",
    ])

    src_redirects = navigation.collect_src_redirects([pj for pj, pdm in pages])
    url_mapping = navigation.build_and_check_url_mapping(pages, src_redirects)
    navigatable: list[tuple[page.PageJekyll, page.PageMint]] = []
    pprint.pprint(url_mapping)

    for src_page, dst_descr in pages:
        print(f"Processing {src_page.descr.rel_path} ...")
        dst_path = dst_root / dst_descr.rel_path
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_page = content.convert_page(src_page, dst_descr, url_mapping, src_root)
        if not src_page.descr.is_fragment and src_page.fm.is_navigatable:
            navigatable.append((src_page, dst_page))
        p_raw = page.render_page_mint(dst_page)
        # if dst_path.exists():
        #     raise Exception(f"destination path {dst_path} already exists.")
        dst_path.write_text(p_raw)
        print(f"... done as {dst_descr.rel_path}")

    copy_assets(src_root, dst_root, [
        "**/*.mdx",
    ], skip_globs=[
        "_site/**/*",
        "_site/*",
    ])

    print(f"Processed {len(pages)} files")

    docs = json.loads((dst_root / "docs.json").read_text())

    leaders2groups = {
        "md": {g["pages"][0]: g for g in navigation.build_navigation_tree(navigatable).to_json()["pages"]},
        "mdx": {g["pages"][0]: g for g in docs["navigation"]["tabs"][0]["pages"]}
    }

    docs_groups = []
    for k, v in sorted(documentation_top_level_groups.items(), key=lambda x: x[1]["pos"]):
        docs_groups.append(leaders2groups[v["src"]][k])

    fbcore_groups = []
    for k, v in sorted(firebolt_core_top_level_groups.items(), key=lambda x: x[1]["pos"]):
        fbcore_groups.append(leaders2groups[v["src"]][k])

    docs["navigation"]["tabs"][0]["pages"] = docs_groups
    docs["navigation"]["tabs"][1]["pages"] = fbcore_groups

    # TODO: postprocess pages based on the navigation tree and rendered contents

    redirects = [{"source": "/godocs/:slug*",
                  "destination": "/:slug*",
                  "permanent": False}]
    for k, v in url_mapping.items():
        if k == v or k.endswith(".md") or k in ("/", "/index", "/index.html"):
            continue
        redirects.append({"source": k,
                          "destination": v,
                          "permanent": False})
    redirects.sort(key=lambda r: (len(r["source"]), r["source"]), reverse=True)
    docs["redirects"] = redirects

    docs_json = json.dumps(docs, indent=2)
    (dst_root / "docs.json").write_text(docs_json + "\n")

    print("DONE")


if __name__ == "__main__":
    main()
