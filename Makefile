start-local:
	scripts/start-local.sh

check-markers:
	scripts/check_merge_conflict_markers.sh .

check-all:
	scripts/check-links.sh
	scripts/check_merge_conflict_markers.sh .

package-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py

package-missing-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py --missing-only

setup-python:
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install requests
	.venv/bin/python -m pip install -r scripts/requirements.txt

clean:
	rm -rf .venv
