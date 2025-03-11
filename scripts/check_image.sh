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
  # Extract all potential img tags (even if missing the opening "<")
  while IFS= read -r tag; do
    trimmed_tag=$(echo "$tag" | xargs)
    tag_errors=""

    # --- Basic Tag Checks ---
    # Check that the tag starts with "<img"
    if [[ "$trimmed_tag" != \<img* ]]; then
      tag_errors+="Missing opening '<' for img tag. "
    fi

    # Check for presence of required attribute names.
    if [[ "$trimmed_tag" != *src=* ]]; then
      tag_errors+="Missing 'src=' attribute. "
    fi
    if [[ "$trimmed_tag" != *alt=* ]]; then
      tag_errors+="Missing 'alt=' attribute. "
    fi
    if [[ "$trimmed_tag" != *width=* ]]; then
      tag_errors+="Missing 'width=' attribute. "
    fi

    # --- Attribute Value Checks (if the attribute exists) ---
    # Only attempt extraction if "src=" is present.
    if [[ "$trimmed_tag" == *src=* ]]; then
      src_value=$(echo "$trimmed_tag" | sed -E 's/.*src=("[^"]+"|'\''[^'\'']+'\''|[^[:space:]>]+).*/\1/')
      src_value=$(echo "$src_value" | sed -E 's/^["'\''](.*)["'\'']$/\1/')
      if [[ -z "$src_value" ]]; then
        tag_errors+="Empty src attribute. "
      elif [[ "$src_value" != *assets/images/* ]]; then
        tag_errors+="src attribute does not include assets/images/. "
      fi
    fi

    if [[ "$trimmed_tag" == *alt=* ]]; then
      alt_value=$(echo "$trimmed_tag" | sed -E 's/.*alt=("[^"]+"|'\''[^'\'']+'\''|[^[:space:]>]+).*/\1/')
      alt_value=$(echo "$alt_value" | sed -E 's/^["'\''](.*)["'\'']$/\1/')
      if [[ -z "$alt_value" ]]; then
        tag_errors+="Empty alt attribute. "
      fi
    fi

    if [[ "$trimmed_tag" == *width=* ]]; then
      width_value=$(echo "$trimmed_tag" | sed -E 's/.*width=("[0-9]+"|'\''[0-9]+'\''|[0-9]+).*/\1/')
      width_value=$(echo "$width_value" | sed -E 's/^["'\''](.*)["'\'']$/\1/')
      if [[ -z "$width_value" ]]; then
        tag_errors+="Empty width attribute. "
      elif ! [[ "$width_value" =~ ^[0-9]+$ ]]; then
        tag_errors+="Width attribute is not numeric. "
      fi
    fi

    # Report all accumulated format errors for this tag.
    if [[ -n "$tag_errors" ]]; then
      echo "Incorrect tag format in file '$md_file':"
      echo "  $trimmed_tag"
      echo "  Errors: $tag_errors"
      FORMAT_ERROR_COUNT=$((FORMAT_ERROR_COUNT+1))
    fi

    # --- Existence Check ---
    # Only do this if src_value was extracted.
    if [[ -n "${src_value:-}" ]]; then
      filename=$(basename "$src_value")
      # Search recursively under IMG_DIR for the file.
      found=$(find "$IMG_DIR" -type f -name "$filename" -print -quit)
      if [[ -z "$found" ]]; then
        echo "Image not found for tag in file '$md_file':"
        echo "  $trimmed_tag"
        echo "  Searched for file: $filename under $IMG_DIR"
        MISSING_COUNT=$((MISSING_COUNT+1))
      fi
    fi

  done < <(grep -oE '(<?)img[^>]*>' "$md_file" || true)
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
