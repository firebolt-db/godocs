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
Just add your single query as a sql file in `docs/_includes/sql_examples`. You can then add the following to your main markdown page:

```
{% include query-window.html sql_file="sql_examples/<your file>" %}
```

For example:

```
{% include query-window.html sql_file="sql_examples/median_example_1.sql" %}
```

You then need to pre-package results for that example or CI will fail.

### How to package documentation examples
If the Firebolt docs server is unavailable (or rate limited), we still want to keep the examples interactive, so we pre-package the results of the examples.
These are also used on the initial page to show example results as quickly as possible.

To package all examples, run:
```bash
make package-docs
```

To package only missing examples, run:
```bash
make package-missing-docs
```

## License summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License.

For details, see the LICENSE file. Any sample code within this documentation is made available under a modified MIT license. For details, see the LICENSE-SAMPLECODE.md file.
