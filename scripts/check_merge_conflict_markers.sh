#!/bin/bash
if [[ $# -eq 0 ]]; then
    echo "Please provide the directory to check. Exiting..."
    exit 1
fi
has_markers=false
# Iterate over all files in the directory given as an argument
for file in "$1"/*; do
    # Skip if the file is called check_merge_conflict_markers.sh
    if [[ "$(basename "$file")" == "check_merge_conflict_markers.sh" ]]; then
        continue
    fi
    # Check if the file is a regular file
    if [[ -f "$file" ]]; then
        # Check if the file contains Git merge conflict markers
        if grep -q "<<<<<<< HEAD" "$file" || grep -q -x "=======" "$file" || grep -q ">>>>>>> " "$file"; then
            echo "Merge conflict markers found in file: $file"
            has_markers=true
        fi
    elif [[ -d "$file" ]]; then
        # Recursively iterate through subdirectories
        if ! "$0" "$file"; then
            has_markers=true
        fi
    fi
done

if $has_markers; then
    exit 1
fi