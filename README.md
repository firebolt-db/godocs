# Firebolt 2.0 documentation repository

Welcome to the open source version of the documentation for the Firebolt Analytics data warehouse. You can submit feedback on the documentation by submitting issues in this repository. You can also propose changes directly by editing files and submitting a pull request.

## How to run locally
Run the following command:
```bash
make start-local
```

Then, you can go to http://localhost:8080/ in your browser to preview the documentation.

## How to check links
```bash
make check-links
```

## How to add an interactive example
We have interactive examples in the documentation. These run against a Firebolt docs server.
1. Add `import {QueryWindow} import {QueryWindow} from '/snippets/query-window.mdx';` at the top of the page if its not yet there.
2. Add `<QueryWindow content={{"sql": "..(your SQL here)..", "result": ..(your result here)..}} />` where you want an interactive example on the page. For example:

```mdxjs
import {QueryWindow} from '/snippets/query-window.mdx';

<QueryWindow content={{
  "sql": "SELECT ABS(-200.50) as result;",
  "result": {
    "data": [
      [
        200.5
      ]
    ],
    "meta": [
      {
        "name": "result",
        "type": "double"
      }
    ],
    "query": {
      "query_id": "7eab6ce7-0174-4e01-adee-2765f715d70a",
      "query_label": null,
      "request_id": "02476fa1-b9ae-4ece-9606-84cee56a595b"
    },
    "rows": 1,
    "statistics": {
      "bytes_read": 1,
      "elapsed": 0.009298,
      "rows_read": 1,
      "scanned_bytes_cache": 0,
      "scanned_bytes_storage": 0,
      "time_before_execution": 0.00025336,
      "time_to_execute": 9.5656e-05
    }
  }
}} />

```

You can leave the `result` part empty and generate it using `make package-missing-docs`.

## Validation System

This repository includes a comprehensive validation system that runs both locally and in CI/CD to ensure documentation quality and consistency.

### Local Validation

Run all validation checks locally with:
```bash
make check-all
```

This runs four main categories of checks:

#### 1. Merge Conflict Markers (`make check-markers`)
- Scans all files for Git merge conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- Prevents accidental commits of unresolved conflicts

#### 2. Navigation Structure (`make check-navigation`)
- **Group Structure**: Validates that pages in docs.json follow proper hierarchical organization
- **Lost Pages**: Identifies MDX files not referenced in navigation or hidden_pages.json
- **Redirect Loops**: Detects circular redirects that would break navigation
- **Lost Redirects**: Ensures all previously known URLs have proper redirects

#### 3. Link Validation (`make check-links`)
- **Internal Links**: Uses Mintlify's built-in broken link checker
- **External Links**: Runs a Docker-based crawler (muffet) to validate external URLs

#### 4. SQL Example Validation (`make check-sql`)
- Validates QueryWindow components against live Firebolt staging API
- Ensures SQL examples produce expected results
- Normalizes results to handle dynamic values (UUIDs, timestamps, etc.)

### GitHub Workflow Validation

The `.github/workflows/pr-check.yml` workflow runs four parallel jobs on every pull request:

1. **check-basic-errors**: Merge conflict markers, legacy directory checks, navigation validation
2. **check-broken-links**: Internal link validation using Mintlify
3. **check-links-using-crawler**: External link validation (informational, doesn't block merge)
4. **check-sql-examples**: SQL example validation (informational, doesn't block merge)

Each job posts status comments on the PR with detailed error information if validation fails.

### Registry Files

#### hidden_pages.json
Tracks pages that exist in the repository but should be excluded from navigation. Each entry requires:
- `path`: Relative path to the MDX file
- `reason`: Explanation for why the page is hidden (e.g., "in private preview", "not yet implemented")

Pages in this file are excluded from the "lost pages" validation check.

#### known_pages.json
Maintains a comprehensive list of all URLs that have ever existed in the documentation. This enables:
- Detection of broken redirects when pages are moved or removed
- Automatic redirect validation to prevent 404 errors
- Historical URL tracking for SEO and bookmark preservation

The file is automatically updated by running `make check-lost-redirects-regenerate`.

### Additional Validation Tools

- **SQL Result Generation**: `make package-missing-docs` automatically generates results for QueryWindow components
- **Python Environment**: `make setup-python` installs validation script dependencies
- **Local Development**: `make start-local` runs Mintlify dev server with live validation

## Contributing Guides

For detailed guidance on contributing to the documentation, see the following guides:

- **[Adding New Pages](contributing-guides/adding-pages.md)**: Step-by-step guide for creating new documentation pages
- **[SQL Examples](contributing-guides/sql-examples.md)**: Working with interactive SQL examples and QueryWindow components  
- **[Moving Pages](contributing-guides/moving-pages.md)**: Safely reorganizing content while maintaining redirects

These guides provide comprehensive instructions for common documentation tasks, including validation requirements, best practices, and troubleshooting tips.

## License summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License.

For details, see the LICENSE file. Any sample code within this documentation is made available under a modified MIT license. For details, see the LICENSE-SAMPLECODE.md file.
