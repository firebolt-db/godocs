SHELL := bash

# .ONESHELL and multi-line recipes require GNU Make 4.2+ (.FEATURES includes "oneshell").
ifeq ($(filter oneshell,$(.FEATURES)),)
$(error \
  GNU Make 4.2+ is required (found: $(or $(MAKE_VERSION),non-GNU make)). \
  On macOS: brew install make, then run gmake or add \
  /opt/homebrew/opt/make/libexec/gnubin to PATH)
endif

.ONESHELL:
.PHONY:

.SHELLFLAGS := -euo pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

MINT := npx -y mint@latest
MUFFET_GO_PKG := github.com/raviqqe/muffet/v2@v2.11.0
MUFFET_DOCKER := raviqqe/muffet:2.11.0
MUFFET_BIN_DIR := $(CURDIR)/.bin
MUFFET_BIN := $(MUFFET_BIN_DIR)/muffet

.PHONY: default
default: check-all


.PHONY: check-all
check-all: check-markers check-navigation-regenerate check-links check-sql


.PHONY: check-navigation
check-navigation: \
	test-checks \
	check-group-structure \
	check-lost-pages \
	check-redirect-loops \
	check-lost-redirects


.PHONY: check-navigation-regenerate
check-navigation-regenerate: \
	test-checks \
	check-group-structure \
	check-lost-pages \
	check-redirect-loops \
	check-lost-redirects-regenerate


.PHONY: start-local
start-local:
	cd docs-mdx && $(MINT) dev


.PHONY: check-links
check-links: check-internal-links check-links-using-crawler


.PHONY: check-internal-links
check-internal-links:
	@echo "Checking internal links integrity..."
	set -euo pipefail
	cd docs-mdx
	tmpf=$$(mktemp)
	$(MINT) broken-links 2>&1 | tee "$$tmpf"
	if egrep -e "found [0-9]+ broken links" "$$tmpf"; then
		exit 1
	else
		echo "☑ Internal links are OK"
	fi


.PHONY: check-links-using-crawler
check-links-using-crawler:
	@echo "Checking external links integrity via crawler..."
	set -euo pipefail
	cd docs-mdx
	if pgrep -f '[m]int.* dev' >/dev/null; then
		echo 'Stopping existing mint dev preview...' 1>&2
		pkill -2 -f '[m]int.* dev' || true
		sleep 2
	fi
	$(MINT) dev --no-open &
	trap "pgrep -f '[m]int.* dev' | xargs kill -2 2>/dev/null || true" EXIT
	echo 'Waiting for mint preview at http://127.0.0.1:3000/intro ...' 1>&2
	deadline=$$((SECONDS + 120))
	http_code=
	while (( SECONDS < deadline )); do
		http_code=$$(curl -s -o /dev/null -w '%{http_code}' 'http://127.0.0.1:3000/intro' || true)
		if [[ "$$http_code" == "200" ]]; then
			break
		fi
		sleep 2
	done
	if [[ "$$http_code" != "200" ]]; then
		echo "mint dev did not become ready (last HTTP status: $${http_code:-none})" 1>&2
		exit 1
	fi
	echo "Service ready on http://127.0.0.1:3000" 1>&2
	muffet_url='http://127.0.0.1:3000'
	muffet_exclude='https://twitter[.]com/.*|https://(.*[.]|)mintlify[.](com|app)[/?].*|https://regex101[.]com|https://signin[.]aws[.]amazon[.]com/.*|sitemap\.xml'
	if [[ "$$(uname -s)" == "Darwin" ]]; then
		# Docker Desktop cannot use --network host; run muffet natively against localhost.
		if [[ ! -x '$(MUFFET_BIN)' ]]; then
			if ! command -v go >/dev/null; then
				echo 'Go is required on macOS to install muffet (brew install go)' 1>&2
				exit 1
			fi
			echo "Installing muffet to $(MUFFET_BIN_DIR) ..." 1>&2
			GOBIN='$(MUFFET_BIN_DIR)' go install $(MUFFET_GO_PKG)
		fi
		'$(MUFFET_BIN)' \
			"--exclude=$$muffet_exclude" \
			--color=auto \
			--buffer-size=100000 \
			--max-connections=2 \
			--max-connections-per-host=2 \
			--ignore-fragments \
			--timeout=60 \
			--max-retries=5 \
			--max-response-body-size=100000000 \
			--accepted-status-codes=200..300,401,402,403,429,500..600 \
			"$$muffet_url"
	else
		docker run --network host $(MUFFET_DOCKER) \
			"--exclude=$$muffet_exclude" \
			--color=auto \
			--buffer-size=100000 \
			--max-connections=5 \
			--max-connections-per-host=5 \
			--ignore-fragments \
			--timeout=30 \
			--max-retries=5 \
			--max-response-body-size=100000000 \
			--accepted-status-codes=200..300,401,402,403,429,500..600 \
			"$$muffet_url"
	fi
	@echo "☑ External links are OK"


.PHONY: check-markers
check-markers:
	@echo "Checking merge conflict markers..."
	scripts/check_merge_conflict_markers.sh .
	@echo "☑ No merge conflict markers found"


.PHONY: check-legacy-dir
check-legacy-dir:
	@echo "Checking that the legacy /docs directory is not resurrected"
	if [ -d "docs" ]; then echo "Legacy /docs directory found, please remove it."; exit 1; fi
	@echo "☑ No /docs directory found"


.PHONY: check-group-structure
check-group-structure: setup-python
	@echo "Checking navigation groups and directories consistency..."
	.venv/bin/python scripts/check_group_structure.py
	@echo "☑ Navigation groups and directories are consistent"


.PHONY: check-lost-pages
check-lost-pages: setup-python
	@echo "Checking for lost pages..."
	.venv/bin/python scripts/check_lost_pages.py
	@echo "☑ No lost pages found"


.PHONY: check-redirect-loops
check-redirect-loops: setup-python
	@echo "Checking for redirect loops..."
	.venv/bin/python scripts/check_redirect_loops.py
	@echo "☑ No redirect loops found"


.PHONY: check-lost-redirects
check-lost-redirects: setup-python
	@echo "Checking for lost redirects..."
	.venv/bin/python scripts/check_lost_redirects.py
	@echo "☑ No lost redirects found"


.PHONY: check-lost-redirects-regenerate
check-lost-redirects-regenerate: setup-python
	@echo "Checking for lost redirects..."
	.venv/bin/python scripts/check_lost_redirects.py regenerate
	@echo "☑ No lost redirects found, known_pages.json updated"


.PHONY: check-sql
check-sql: setup-python
	@echo "Checking SQL examples..."
	.venv/bin/python scripts/check_sql_examples.py quiet
	@echo "☑ SQL examples are working"


.PHONY: test-checks
test-checks: setup-python
	@echo "Testing check scripts..."
	.venv/bin/python -m pytest -q scripts/*_test.py
	@echo "☑ Check scripts working"


.PHONY: package-docs
package-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py


.PHONY: package-missing-docs
package-missing-docs: setup-python
	.venv/bin/python scripts/prepackage_query_results.py --missing-only


.PHONY: setup-python
setup-python:
	if [[ `python3 --version | cut -d '.' -f 2` < 10 ]]; then echo "Need at least python3.10, you have:"; python3 --version; exit 1; fi;
	if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r scripts/requirements.txt

clean:
	rm -rf .venv
