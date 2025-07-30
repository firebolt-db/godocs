from pathlib import Path
import pytest

import scripts.check_sql_examples as cse


@pytest.mark.parametrize(["root_dir"], [(x,) for x in
    (Path(__file__).parent / "test_data" / "check_sql_examples").glob("*/")
])
def test_check_sql_examples(root_dir, monkeypatch):
    def fake_fetch(sql: str):
        return {
            "data": [[2]],
            "query": {"query_id": "id", "request_id": "r", "query_label": "l"},
            "statistics": {"elapsed": "0"}
        }

    monkeypatch.setattr(cse, "fetch_real_sql", fake_fetch)
    with pytest.raises(cse.SqlExamplesError):
        cse.main(root_dir, [])
