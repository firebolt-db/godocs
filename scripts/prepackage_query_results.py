import contextlib
import json
import re
import textwrap
import time
import requests
import argparse
from pathlib import Path


@contextlib.contextmanager
def ensure_delay(delay=0.1):
    start_time = time.time()
    yield
    elapsed = time.time() - start_time
    if elapsed < delay:
        time.sleep(delay - elapsed)


def execute_query(query):
    with ensure_delay():
        try:
            response = requests.post(
                'https://api.staging.firebolt.io/demo/execute-query',
                headers={'Content-Type': 'application/json'},
                json={'query': query},
                timeout=10
            )
            try:
                return response.json()
            except json.JSONDecodeError:
                print(f"Error decoding JSON response (status code: {response.status_code})")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error executing query: {e}")
            return None


def process_md_sql_examples(root: Path, missing_only: bool):
    # Process SQL files
    for sql_file in root.glob('docs/_includes/sql_examples/*.sql'):
        json_file = sql_file.with_suffix('.json')

        # Skip if JSON exists and we're in missing-only mode
        if missing_only and json_file.exists():
            print(f"Skipping {sql_file.name} (JSON exists)")
            continue

        print(f"Processing {sql_file.name}...")

        # Read SQL query
        query = sql_file.read_text().strip()

        # Execute query
        result = execute_query(query)

        if result:
            # Save result
            json_file.write_text(json.dumps(result, indent=2))
            print(f"Saved result to {json_file.name}")
        else:
            print(f"Failed to get result for {sql_file.name}")


def format_query_window_content(content: dict) -> str:
    return f'{{\n  "sql": {json.dumps(content["sql"])},\n  "result": {textwrap.indent(json.dumps(content["result"], indent=2, sort_keys=True), "  ").lstrip()}\n}}'


def process_mdx_sql_examples(root: Path, missing_only: bool):
    def process_example(f: Path, match: re.Match):
        t = time.time()
        content = json.loads(match.group(2))
        sql = content['sql']
        result = content.get('result', None)
        # Skip if JSON exists and we're in missing-only mode
        if missing_only and result is not None:
            print(f"Skipping {sql} (JSON exists)")
            return match.group(0)
        print(f"Processing {f} / {repr(sql)} ...")
        # Execute query
        content['result'] = execute_query(sql)
        res = f'{match.group(1)}{format_query_window_content(content)}{match.group(3)}'
        print("Updated result in example")
        return res

    for mdx_file in root.glob('docs-mdx/**/*.mdx'):
        cont = mdx_file.read_text()
        cont_sub = re.sub(r'(<QueryWindow\s+content=\{)(\{.*?\})(\}\s+/>)', lambda x: process_example(mdx_file, x), mdx_file.read_text(), flags=re.DOTALL)
        if cont != cont_sub:
            mdx_file.write_text(cont_sub)
            print(f"Updated {mdx_file} with processed examples")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--missing-only', action='store_true', 
                       help='Only process SQL files that don\'t have corresponding JSON files')
    parser.add_argument('--doc-type', required=True, choices=['md', 'mdx'],
                       help='Process SQL examples from Markdown (md) or MDX (mdx) files')
    args = parser.parse_args()
    if args.doc_type == 'md':
        process_md_sql_examples(Path('.'), args.missing_only)
    elif args.doc_type == 'mdx':
        process_mdx_sql_examples(Path('.'), args.missing_only)
    print("Done")


if __name__ == '__main__':
    main() 