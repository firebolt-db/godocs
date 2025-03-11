#!/bin/bash
set -euo pipefail

# Get the directory of this script.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# ROOT_DIR is one level above the scripts folder (i.e. firebolt-docs-staging)
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Define the docs and images directories.
DOCS_DIR="${ROOT_DIR}/docs"
IMG_DIR="${DOCS_DIR}/assets/images"

# Counters for errors.
FORMAT_ERROR_COUNT=0
MISSING_COUNT=0

echo "🔍 Checking image tags in Markdown files under ${DOCS_DIR} ..."

# Loop through every Markdown file under docs.
while IFS= read -r md_file; do
  # Extract all <img ...> tags from the file.
  while IFS= read -r tag; do
    # Remove extra whitespace.
    trimmed_tag=$(echo "$tag" | xargs)

    # --- Format Checks ---
    # Extract src attribute value (allow quotes or not).
    src_value=$(echo "$trimmed_tag" | sed -E 's/.*src=("[^"]+"|'\''[^'\'']+'\''|[^[:space:]>]+).*/\1/')
    src_value=$(echo "$src_value" | sed -E 's/^["'\''](.*)["'\'']$/\1/')
    if [[ -z "$src_value" ]]; then
      echo "Missing src attribute in file '$md_file':"
      echo "  $trimmed_tag"
      FORMAT_ERROR_COUNT=$((FORMAT_ERROR_COUNT+1))
      continue
    fi
    if [[ "$src_value" != *assets/images/* ]]; then
      echo "src attribute does not include assets/images/ in file '$md_file':"
      echo "  $trimmed_tag"
      FORMAT_ERROR_COUNT=$((FORMAT_ERROR_COUNT+1))
      continue
    fi

    # Extract alt attribute value.
    alt_value=$(echo "$trimmed_tag" | sed -E 's/.*alt=("[^"]+"|'\''[^'\'']+'\''|[^[:space:]>]+).*/\1/')
    alt_value=$(echo "$alt_value" | sed -E 's/^["'\''](.*)["'\'']$/\1/')
    if [[ -z "$alt_value" ]]; then
      echo "Missing or empty alt attribute in file '$md_file':"
      echo "  $trimmed_tag"
      FORMAT_ERROR_COUNT=$((FORMAT_ERROR_COUNT+1))
      continue
    fi

    # Extract width attribute value (must be numeric).
    width_value=$(echo "$trimmed_tag" | sed -E 's/.*width=("[0-9]+"|'\''[0-9]+'\''|[0-9]+).*/\1/')
    width_value=$(echo "$width_value" | sed -E 's/^["'\''](.*)["'\'']$/\1/')
    if [[ -z "$width_value" ]]; then
      echo "Missing width attribute in file '$md_file':"
      echo "  $trimmed_tag"
      FORMAT_ERROR_COUNT=$((FORMAT_ERROR_COUNT+1))
      continue
    fi
    if ! [[ "$width_value" =~ ^[0-9]+$ ]]; then
      echo "Width attribute is not numeric in file '$md_file':"
      echo "  $trimmed_tag"
      FORMAT_ERROR_COUNT=$((FORMAT_ERROR_COUNT+1))
      continue
    fi

    # --- Existence Check ---
    # Extract the filename from the src attribute.
    filename=$(basename "$src_value")
    # Search recursively under the images directory for the file.
    found=$(find "$IMG_DIR" -type f -name "$filename" -print -quit)
    if [[ -z "$found" ]]; then
      echo "Image not found for tag in file '$md_file':"
      echo "  $trimmed_tag"
      echo "  Searched for file: $filename under $IMG_DIR"
      MISSING_COUNT=$((MISSING_COUNT+1))
    fi

  done < <(grep -oE '<img[^>]+>' "$md_file" || true)
done < <(find "$DOCS_DIR" -type f -name "*.md")

# Summary output.
if [[ $FORMAT_ERROR_COUNT -eq 0 && $MISSING_COUNT -eq 0 ]]; then
  echo "✅ All image tags are correctly formatted and all referenced images exist."
else
  if [[ $FORMAT_ERROR_COUNT -ne 0 ]]; then
    echo "⚠️ Found $FORMAT_ERROR_COUNT image tag(s) with incorrect format."
  fi
  if [[ $MISSING_COUNT -ne 0 ]]; then
    echo "⚠️ Found $MISSING_COUNT image reference(s) where the file is missing."
  fi
  exit 1
fi
