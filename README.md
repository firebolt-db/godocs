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

## License summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License.

For details, see the LICENSE file. Any sample code within this documentation is made available under a modified MIT license. For details, see the LICENSE-SAMPLECODE.md file.
