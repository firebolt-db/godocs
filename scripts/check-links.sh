#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(realpath -eP "$(dirname -- "${BASH_SOURCE[0]}")")"
ROOT_DIR="$(realpath -eP "${SCRIPT_DIR}/..")"

. "$SCRIPT_DIR/_common.sh"
build_all "$ROOT_DIR" -q >& 2
run "$ROOT_DIR" link-check
