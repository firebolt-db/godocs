#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(realpath -eP "$(dirname -- "${BASH_SOURCE[0]}")")"
ROOT_DIR="$(realpath -eP "${SCRIPT_DIR}/..")"

. "$SCRIPT_DIR/_common.sh"

run "$ROOT_DIR" --build -P -v "$ROOT_DIR:/www" localhost-firebolt-docs
