#!/usr/bin/env python3
import contextlib
import difflib
import json
import pathlib
import re
import sys
import time
from typing import Any

import requests


@contextlib.contextmanager
def ensure_delay(delay=0.1):
    start_time = time.time()
    yield
    elapsed = time.time() - start_time
    if elapsed < delay:
        time.sleep(delay - elapsed)


def fetch_real_sql(sql: str) -> Any:
    with ensure_delay():
        result = requests.post(
            url='https://api.staging.firebolt.io/demo/execute-query', json={'query': sql}, timeout=10).json()
        # Enforce minimum execution time to avoid hitting the API too fast
        return result


def normalize_result(sql: str, result: Any):
    for key in ['query_id', 'request_id', 'query_label']:
        result['query'][key] = "<redacted>"
    for key in ['elapsed', 'time_before_execution', 'time_to_execute', 'bytes_read', 'scanned_bytes_cache', 'scanned_bytes_storage']:
        result['statistics'][key] = "<redacted>"
    if 'gen_random_uuid_text()' in sql.lower():
        for row in result.get('data', []):
            for i in range(len(row)):
                if re.match("^[a-f0-9]{8}-(?:[a-f0-9]{4}-){3}[a-f0-9]{12}$", str(row[i])):
                    row[i] = "<redacted>"
    if 'random()' in sql.lower():
        for row in result.get('data', []):
            for i in range(len(row)):
                if isinstance(row[i], (float, int)):
                    row[i] = "<redacted>"


def compare_results(sql: str, expected: Any, actual: Any) -> list[str]:
    normalize_result(sql, expected)
    normalize_result(sql, actual)
    return list(difflib.unified_diff(
        json.dumps(expected, indent=2, sort_keys=True).splitlines(),
        json.dumps(actual, indent=2, sort_keys=True).splitlines()))


class ResultsDiffError(Exception):
    def __init__(self, path: pathlib.Path, sql: str, expected: Any, actual: Any):
        super().__init__(f"Differences found in {path}:\n{sql}\n{"\n".join(compare_results(sql, expected, actual))}"
                         f"\nExpected result:\n{json.dumps(expected, indent=2)}"
                         f"\nActual result:\n{json.dumps(actual, indent=2)}")
        self.path = path
        self.sql = sql
        self.expected = expected
        self.actual = actual


def check_md_sql_examples(doc_dir: pathlib.Path, to_check: list[str]) -> list[tuple[pathlib.Path, Exception]]:
    res = []
    for ex in sorted(doc_dir.glob("**/*.sql") if not to_check else map(pathlib.Path, to_check)):
        try:
            print(f"Checking {ex.relative_to(doc_dir.parent)} ...")
            expected = json.loads(ex.with_suffix(".json").read_text())
            sql = ex.read_text()
            actual = fetch_real_sql(sql)
            if compare_results(sql, expected, actual):
                raise ResultsDiffError(ex, sql, expected, actual)
            print("OK")
        except Exception as e:
            res.append((ex, e))
            print(f"Error checking {ex}: {e}")
    return res


def check_mdx_sql_examples(doc_dir: pathlib.Path, to_check: list[str]) -> list[tuple[pathlib.Path, Exception]]:
    res = []
    for ex in sorted(doc_dir.glob("**/*.mdx") if not to_check else map(pathlib.Path, to_check)):
        try:
            for ex_attr in re.finditer(r'<QueryWindow\s+content=\{(\{.*?\})\}\s+/>', ex.read_text(), re.DOTALL):
                ex_attr = json.loads(ex_attr.group(1))
                sql = ex_attr['sql']
                print(f"Checking {ex.relative_to(doc_dir.parent)} / {json.dumps(sql)} ...")
                expected = ex_attr['result']
                actual = fetch_real_sql(sql)
                if compare_results(sql, expected, actual):
                    raise ResultsDiffError(ex, sql, expected, actual)
                print("OK")
        except Exception as e:
            res.append((ex, e))
            print(f"Error checking {ex}: {e}")
    return res


def main():
    to_check = sys.stdin.read().strip().splitlines() if not sys.stdin.isatty() else []
    doc_dir = pathlib.Path(sys.argv[1])
    doc_type = sys.argv[2]
    if doc_type == "md":
        res = check_md_sql_examples(doc_dir, to_check)
    elif doc_type == "mdx":
        res = check_mdx_sql_examples(doc_dir, to_check)
    else:
        print(f"Invalid argument: {doc_dir}")
        sys.exit(1)
    if not res:
        print(f"SQL examples checks passed for .{doc_type} examples in {doc_dir}")
    else:
        print(f"{len(res)} errors found:")
        for ex, e in res:
            print(f"------------\n{ex.relative_to(doc_dir.parent)}\n{e}")
    if res:
        sys.exit(1)


if __name__ == "__main__":
    main()
