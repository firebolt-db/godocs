#!/bin/bash
## generate-redirects.sh
##
## Script to generate a redirect based on souce/destination lists.
##
#

set -e
set -o nounset

if [ $# -ne 2 ]; then
	echo "Usage: generate-redirects.sh source_urls.txt destination_urls.txt" 1>&2
	exit 1
fi

SRC="$1"
DEST="$2"

function generate_index() {
	local URL="$1"
cat<<EOF
<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to ${URL}</title>
<meta http-equiv="refresh" content="0; URL=${URL}">
<link rel="canonical" href="${URL}">
EOF
}

ERRORS=0
I=0
for URL in $(< "$SRC"); do
	I=$[I + 1]
	URI=$(echo "$URL" | sed 's~^https://docs.firebolt.io/~~')

	if echo "$URI" | grep -q ^http; then
		echo "ERROR: source URL at line $I is malformed: $URL" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi

	TARGET_URL="$(sed "${I}q;d" $DEST)"
	if [ -z "$TARGET_URL" ]; then
		echo "ERROR: cannot find URL for source URL at line $I" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi

	if [[ $URI =~ "#" ]]; then
		echo "ERROR: source URL at line $I cannot contain '#'" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi
	if [[ $TARGET_URL =~ "#" ]]; then
		echo "ERROR: destination URL at line $I cannot contain '#'" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi

	if echo "$URI" | grep -q html$; then
		D="$(dirname $URI)"
		FN="$(basename $URI)"
		NAME_NO_EXT="${FN%.*}" # fileanme without path and without extension
	elif echo "$URI" | grep -q /$; then
		# remove last slash
		D="${URI::-1}"
		FN=index.html
		NAME_NO_EXT="$(basename "$D")"
	else
		echo "ERROR: source URL at line $I should end with '/' or '.html'" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi
	D="docs/godocs/$D"

	# make sure that a pre-existing redirect, or a corresponding directory or 'md' file do not already exist
	if [ -f "$D/$FN" ]; then
		echo "ERROR: line $I: $D/$FN already exists" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi
	if [ -d "$D/$NAME_NO_EXT" ]; then
		echo "ERROR: line $I: $D/$NAME_NO_EXT already exists" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi
	if [ -f "$D/${NAME_NO_EXT}.md" ]; then
		echo "ERROR: line $I: $D/${NAME_NO_EXT}.md already exists" 1>&2
		ERRORS=$[ERRORS + 1]
		continue
	fi

	mkdir -p "$D"
	generate_index "$TARGET_URL" > "$D/$FN"

	echo "Created redirect $URI ($D/$FN) -> $TARGET_URL" 1>&2
done

exit $ERRORS
