#!/bin/bash

set -xeuo pipefail

usage="Usage: scripts/$(basename $BASH_SOURCE) <check_name> <required|informational> <check_command...>"
check_name=${1?"$usage"}
shift
required=${1?"$usage"}
failure_comment=""
if [[ required != "required" ]]; then
  failure_comment="(informational check, does not block merge)"
fi
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
  echo "<details>"
  echo "<summary>❌ $check_name $failure_comment</summary>"
  echo '<pre>'
  cat "$tmpf"
  echo '</pre>'
  echo "</details>"
  echo
else
  echo "✅ $check_name"
fi
echo "$tmpf"
exit "$rv"
