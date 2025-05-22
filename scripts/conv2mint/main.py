import shutil
import sys
from pathlib import Path

from content import parse_page, convert_md_page, render_page


def copy_assets(src_root: Path, dst_root: Path, asset_dir: str):
    # TODO: collect asset paths firt, only copy the assets which are actually used
    src_assets = src_root / asset_dir
    dst_assets = dst_root / asset_dir
    if not src_assets.exists():
        raise Exception(f"source assets directory {src_assets} does not exist.")
    shutil.rmtree(dst_assets)
    shutil.copytree(src_assets, dst_assets)
    print(f"Copied assets from {src_assets} to {dst_assets}")


def main():
    if len(sys.argv) < 3 or "--help" in sys.argv:
        print(f"Usage: {sys.argv[0]} <src_root> <dst_root>")
        return

    src_root, dst_root = Path(sys.argv[1]), Path(sys.argv[2])
    copy_assets(src_root, dst_root, "assets")

    doc_dirs = [
        "Overview",
        "Guides",
        "integrations",
        "Reference",
        "sql_reference"
    ]
    for d in doc_dirs:
        # TODO: beautiful paths in urls
        src_d = src_root / d
        dst_d = dst_root / d

        shutil.rmtree(dst_d, ignore_errors=True)

        for f in src_d.rglob('**/*.md'):
            print(f"converting {f.relative_to(src_root)}...")
            # TODO: create a redirect for the old path
            rel_dir= f.relative_to(src_d).parent
            rel_path = rel_dir / f.name
            dst_dir = dst_d / rel_dir
            dst_name = f.name + "x"
            dst_path = dst_dir / dst_name
            dst_dir.mkdir(parents=True, exist_ok=True)
            p = parse_page(f.read_text(), rel_path)
            p_conv = convert_md_page(p)
            p_raw = render_page(p_conv)
            dst_path.write_text(p_raw)
            print("Done")

if __name__ == "__main__":
    main()
