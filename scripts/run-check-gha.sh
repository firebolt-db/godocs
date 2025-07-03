#!/bin/bash

set -xeuo pipefail

usage="Usage: scripts/$(basename $BASH_SOURCE) <check_name> <failure_comment> <check_command...>"
check_name=${1?"$usage"}
shift
failure_comment=${1?"$usage"}
shift
check_cmd=${1?"$usage"}
shift
check_args=$@

set +e
tmpf=$(mktemp)
"$check_cmd" "${check_args[@]}" >"$tmpf" 2>&1
rv=$?
set -e
cat "$tmpf" >&2

# Abusing the unique name of the file as an EOF marker
echo "output<<$tmpf"
if [[ "$rv" != 0 ]]; then
  echo "❌ $check_name: FAILURE $failure_comment"
  echo "<details>"
  echo "<summary>Click to expand</summary>"
  echo '<pre>'
  cat "$tmpf"
  echo '</pre>'
  echo "</details>"
  echo
else
  echo "✅ $check_name: SUCCESS"
fi
echo "$tmpf"
exit "$rv"
