SHELL := bash

.ONESHELL:
.PHONY:

.SHELLFLAGS := -euo pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


.PHONY: default
default: check-all


.PHONY: check-all
check-all: check-markers check-nav-structure check-links check-sql


.PHONY: start-local
start-local: maybe-setup-mint
	cd docs-mdx && mint dev


.PHONY: check-links
check-links: maybe-setup-mint
	set -euo pipefail
	cd docs-mdx
	mint broken-links
	mint dev --no-open &
	pid=$$!
	tmpf=$$(mktemp)
	trap "kill $$pid; rm $$tmpf" EXIT
	while ! curl -s 'http://localhost:3000/' >/dev/null; do
		echo 'Waiting the service to start on localhost:3000' 1>&2
		sleep 1
	done
	(docker run --network host raviqqe/muffet \
		"--exclude=https://twitter.com/.*|https://mintlify.mintlify.app/.*|https://regex101.com|https://signin.aws.amazon.com/.*" \
		--color=auto \
		--buffer-size=100000 \
		--max-connections=5 \
		--ignore-fragments \
		--timeout=30 \
		--max-response-body-size=100000000 \
		--accepted-status-codes=200..300,403 \
		http://localhost:3000 >> "$$tmpf" 2>&1) || (cat "$$tmpf" && exit 1)


.PHONY: check-markers
check-markers:
	scripts/check_merge_conflict_markers.sh .


.PHONY: check-legacy-dir
check-legacy-dir:
	if [ -d "docs" ]; then echo "Legacy /docs directory found, please remove it."; exit 1; fi


.PHONY: check-nav-structure
check-nav-structure: setup-python
	.venv/bin/python scripts/check_nav_structure.py


.PHONY: check-sql
check-sql: setup-python
	.venv/bin/python scripts/check_sql_examples.py quiet


.PHONY: package-docs
package-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py


.PHONY: package-missing-docs
package-missing-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py --missing-only


.PHONY: setup-python
setup-python:
	if [[ `python3 --version | cut -d '.' -f 2` < 12 ]]; then echo "Need at least python3.12, you have:"; python3 --version; exit 1; fi;
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r scripts/requirements.txt


.PHONY: use-python
use-python:
	/bin/bash --rcfile scripts/rcpy -i


.PHONY: setup-mint
setup-mint:
	npm i -g mint


.PHONY: maybe-setup-mint
maybe-setup-mint:
	mint version || npm i -g mint


clean:
	rm -rf .venv
