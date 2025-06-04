SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


.PHONY: default
default: check-markers check-links check-md-mdx-in-sync check-links-mint check-sql


.PHONY: check-all
check-all: check-markers check-links check-sql


.PHONY: check-all-mdx
check-all-mdx: check-markers check-md-mdx-in-sync check-links-mint # check-sql-mdx


.PHONY: sync-docs-md-to-mdx
sync-docs-md-to-mdx: setup-python
	@bash -c '\
		read -p "This will overwrite docs-mdx with the contents of docs. Are you sure? (y/n) " -n 1 -r; echo; \
		if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
			.venv/bin/python scripts/conv2mint/__main__.py docs docs-mdx; \
		else \
			echo "Aborting sync."; \
			exit 1; \
		fi'


.PHONY: check-md-mdx-in-sync
check-md-mdx-in-sync: setup-python
	tmpd=$(shell mktemp -d)
	trap 'rm -rf "$$tmpd"' EXIT
	cp -r docs-mdx/* $$tmpd
	.venv/bin/python scripts/conv2mint/__main__.py docs $$tmpd
	diff -r $$tmpd docs-mdx || (echo "docs-mdx is not in sync with docs, run 'make sync-docs-md-to-mdx' to fix" && exit 1)


.PHONY: start-local
start-local:
	scripts/start-local.sh


.PHONY: start-local-mint
start-local-mint: maybe-setup-mint
	cd docs-mdx && mint dev


.PHONY: check-links
check-links:
	scripts/check-links.sh


.PHONY: check-links-mint
check-links-mint: maybe-setup-mint
	cd docs-mdx && mint broken-links


.PHONY: check-markers
check-markers:
	scripts/check_merge_conflict_markers.sh .


.PHONY: check-sql
check-sql: setup-python
	.venv/bin/python scripts/check_sql_examples.py docs md quiet


.PHONY: check-sql-mdx
check-sql-mdx: setup-python
	.venv/bin/python scripts/check_sql_examples.py docs-mdx mdx quiet


.PHONY: package-docs
package-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py --doc-type md


.PHONY: package-missing-docs
package-missing-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py --missing-only --doc-type md


.PHONY: package-docs-mdx
package-docs-mdx: package-docs sync-docs-md-to-mdx
# commented out while we keep docs-mdx in sync with docs
#package-docs-mdx: setup-python
#	.venv/bin/python scripts/prepackage_query_results.py --doc-type mdx


.PHONY: package-missing-docs-mdx
package-missing-docs-mdx: package-missing-docs sync-docs-md-to-mdx
# commented out while we keep docs-mdx in sync with docs
#package-missing-docs-mdx: setup-python
#	.venv/bin/python scripts/prepackage_query_results.py --missing-only --doc-type mdx


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
	rm -rf .venv docs/_site
