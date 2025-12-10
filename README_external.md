## About this repo
* This repository contains the source code for the Firebolt documentation (https://docs.firebolt.io/).
* Pages are in [MDX format](#about-mdx-format-and-mintlify-platform).
* Pages are hosted on [Mintlify](https://mintlify.com) platform. It offers AI tooling, internal search and AI bot.
* Main branch is `gh-pages`. It is automatically published to https://docs.firebolt.io/.
* Important: To improve the search and AI bot, set great [keywords](https://mintlify.com/docs/pages#internal-search-optimization) and [description](https://mintlify.com/docs/pages#descriptions) as it influences search and AI bot functionality.

## Known problems
* The crawler link checker sometimes would fail on a fetch timeout.

## Quick start
* [Add a new page](#how-to-add-a-new-page).
* [Run local checks](#how-to-check-locally) using `make check-all`.
* [Preview the documentation locally](#how-to-preview-locally) using `make start-local`.
* [Contribute changes](#how-to-contribute-changes).

## Table of contents
<!-- TOC -->
  * [Guides for tooling](#guides-for-tooling)
    * [How to preview locally](#how-to-preview-locally)
    * [How to check locally](#how-to-check-locally)
      * [Merge conflict markers check](#merge-conflict-markers-check)
      * [Navigation structure check](#navigation-structure-check)
      * [Link check](#link-check)
      * [SQL example check](#sql-example-check)
  * [Guides for editing](#guides-for-editing)
    * [How to add a new page](#how-to-add-a-new-page)
    * [How to move an existing page](#how-to-move-an-existing-page)
    * [How to add an interactive SQL example](#how-to-add-an-interactive-sql-example)
    * [How to contribute changes](#how-to-contribute-changes)
  * [Repository structure](#repository-structure)
  * [GitHub PR Workflow](#github-pr-workflow)
  * [About MDX format and Mintlify platform](#about-mdx-format-and-mintlify-platform)
    * [Key differences between MDX and MD formats](#key-differences-between-mdx-and-md-formats)
    * [Mintlify specifics](#mintlify-specifics)
    * [AI tools in Mintlify](#ai-tools-in-mintlify)
    * [Further references](#further-references)
<!-- TOC -->

## Guides for tooling

### How to preview locally
1. Run `make start-local`.
2. Open http://localhost:3000/ in your browser to preview the documentation.

### How to check locally
Use `make check-all` or just `make` to run all checks.

#### Merge conflict markers check
`make check-markers` scans all files for Git merge conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

#### Navigation structure check
`make check-navigation-regenerate` checks the navigation structure and adds all new pages [known_pages.json](known_pages.json).

It runs the following subchecks:
- `make check-group-structure` checks that the pages in [docs-mdx/docs.json](docs-mdx/docs.json) are organized into consistent groups and directory structure mirrors the navigational structure.
- `make check-lost-pages` checks that all MDX files are referenced in [docs-mdx/docs.json](docs-mdx/docs.json) unless they are explicitly listed in [hidden_pages.json](hidden_pages.json).
- `make check-redirect-loops` checks that there are no circular redirects in the documentation.
- `make check-lost-redirects-regenerate` checks that all known URLs (listed in [known_pages.json](known_pages.json)) either have a corresponding page in [docs-mdx/](docs-mdx) or a proper redirect in [docs-mdx/docs.json](docs-mdx/docs.json). It also updates [known_pages.json](known_pages.json) with new URLs.

#### Link check
`make check-links` verifies that no links in the documentation result in 404.

It runs the following subchecks:
  * `make check-internal-links` runs Mintlify's built-in broken link checker and validate internal links in the documentation.
  * `make check-links-using-crawler` to bring up a local site instance using `mint dev` and run [muffet](https://github.com/raviqqe/muffet) link crawler against it.

#### SQL example check
This checks that all `<QueryWindow/>` components in the documentation have pre-generated results.
* `make check-sql` to check that all `<QueryWindow/>` components produce expected results.
* `make package-docs` to regenerate all results for all `<QueryWindow/>` components in the documentation.
* `make package-missing-docs` to generate results for all `<QueryWindow/>` components that don't have pre-generated results.

## Guides for editing
### How to add a new page
1. Before you start
   * Read the [MDX and Mintlify](#about-mdx-format-and-mintlify-platform) guide below.
   * See example at [function-template.mdx](function-template.mdx) or [here](docs-mdx/reference-sql/functions-reference/date-and-time/to-date.mdx).
2. Create the MDX file in the appropriate directory under [docs-mdx/](docs-mdx). Place images in [docs-mdx/assets/images](docs-mdx/assets/images). **No whitespace or upper case is allowed in the path.**
3. **Choose [keywords](https://mintlify.com/docs/pages#internal-search-optimization) and write great [description](https://mintlify.com/docs/pages#descriptions) to help Mintlify's search and AI bot to find the page.**
4. Add the file to the navigation structure in [docs-mdx/docs.json](docs-mdx/docs.json). **The navigation structure must reflect the directory structure.**
5. Run the checks (`make check-all` or `make`) to ensure everything is correct and automatically update the [known_pages.json](known_pages.json) file with the new URL.
6. Preview the page locally using `make start-local`.
7. Push the changes to the repository and open the PR. See [here](#how-to-contribute-changes) for how to contribute changes.

### How to move an existing page
NB: `mint rename` does a terrible job, do not use it.

1. Move the MDX file to the new location in [docs-mdx/](docs-mdx). **No whitespace or upper case is allowed in the path.**
2. Update all cross-references to the page in other MDX files.
3. Update the navigation structure in [docs-mdx/docs.json](docs-mdx/docs.json) with the new location. **The navigation structure must reflect the directory structure.**
4. Run `make check-links` and `make check-links-using-crawler` to find missed links.
5. Add a redirect from the old URL to the new URL in [docs-mdx/docs.json](docs-mdx/docs.json).
6. Run the checks (`make check-all` or `make`) to ensure everything is correct and automatically update the [known_pages.json](known_pages.json) file with the new URL.
7. Preview the page locally using `make start-local`.
8. Further steps as similar to [adding a new page](#how-to-add-a-new-page).

### How to add an interactive SQL example
The interactive examples run against a dedicated Firebolt documentation server. See an example [here](https://docs.firebolt.io/reference-sql/functions-reference/date-and-time/to-date) and its sources [here](docs-mdx/snippets/sql_examples/to_date_executable.mdx) and [here](docs-mdx/reference-sql/functions-reference/date-and-time/to-date.mdx).
1. Add `import {QueryWindow} from '/snippets/query-window.mdx';` at the top of the page if its not yet there. Don't add it more than once.
2. Add `<QueryWindow content={{"sql": "..(your SQL here)..", "result": ..(your result here)..}} />` where you want an interactive example on the page. For example:
    ```mdxjs
    import {QueryWindow} from '/snippets/query-window.mdx';
    
    <QueryWindow content={{
      "sql": "SELECT ABS(-200.50) AS result;",
      "result": {
        "data": [[200.5]],
        "meta": [{"name": "result", "type": "double"}],
        "query": { ... },
        "rows": 1,
        "statistics": { ... }
      }
    }} />
    ```
3. You can leave the `result` part empty and generate it using `make package-missing-docs`.
4. Preview the page locally using `make start-local` to ensure the example works as expected.
5. Further steps as similar to [adding a new page](#how-to-add-a-new-page).

### How to contribute changes
1. Fork the repository to your GitHub account.
2. Create a branch with your changes.
3. Open a pull request with your changes to the `gh-pages` branch.
4. Wait for the CI/CD pipeline to run and address any issues.
5. The repository maintainers will review your PR and provide feedback.
6. Once approved, the maintainers will merge your changes.

## Repository structure
* [docs-mdx/](docs-mdx) contains all the MDX files for the documentation:
  * [docs-mdx/docs.json](docs-mdx/docs.json) defines the navigation structure of the documentation.
  * [docs-mdx/assets/](docs-mdx/assets) contains static assets like images, styles and scripts used in the documentation. All styles and scripts are embedded in the MDX files by mintlify. See [here](https://mintlify.com/docs/settings/custom-scripts). Note: there's no control over their order on the page.
  * [docs-mdx/snippets/](docs-mdx/snippets) contains reusable [snippets](https://mintlify.com/docs/reusable-snippets) and [components](https://mintlify.com/docs/react-components).
* [scripts/](scripts) contains checking scripts and utilities:
  * [scripts/check_group_structure.py](scripts/check_group_structure.py) checks that the pages in [docs-mdx/docs.json](docs-mdx/docs.json) are organized into consistent groups and directory structure mirrors the navigational structure.
  * [scripts/check_lost_pages.py](scripts/check_lost_pages.py) checks that all MDX files are referenced in [docs-mdx/docs.json](docs-mdx/docs.json) unless they are listed in [hidden_pages.json](hidden_pages.json).
  * [scripts/check_redirect_loops.py](scripts/check_redirect_loops.py) checks that there are no circular redirects in the documentation.
  * [scripts/check_lost_redirects.py](scripts/check_lost_redirects.py) checks that all known URLs (listed in [known_pages.json](known_pages.json)) either have a corresponding page in [docs-mdx/](docs-mdx) or a proper redirect in [docs-mdx/docs.json](docs-mdx/docs.json).
  * [scripts/check_sql_examples.py](scripts/check_sql_examples.py) checks that pre-generated results in `<QueryWindow/>` components are the same as the real results.
  * [scripts/check_merge_conflict_markers.sh](scripts/check_merge_conflict_markers.sh) checks that there are no Git merge conflict markers in the documentation files.
* [hidden_pages.json](hidden_pages.json) contains all pages that are intentionally not included in the navigation. This is to prevent accidental hiding of pages by forgetting to add them to [docs-mdx/docs.json](docs-mdx/docs.json).
* [known_pages.json](known_pages.json) contains all URLs that have ever existed in the documentation. This is used to check for lost redirects.
* [function-template.mdx](function-template.mdx) is an example page.

## GitHub PR Workflow

The [.github/workflows/pr-check.yml](.github/workflows/pr-check.yml) workflow runs four parallel jobs on every pull request:

* **check-basic-errors**: Merge conflict markers, legacy directory checks, navigation validation
* **check-broken-links**: Internal link validation using Mintlify
* **check-links-using-crawler**: External link validation (informational, doesn't block merge)
* **check-sql-examples**: SQL example validation (informational, doesn't block merge)

## About MDX format and Mintlify platform
### Key differences between MDX and MD formats
* MDX is JSX-based, meaning:
  * All pages, custom tags and HTML tags are React components. Some HTML tags are not supported.
  * HTML tags need to be closed and lowercase (`<p></p>` instead of `<p>`, `<br/>` instead of `<BR>`).
  * Tag attributes are camel case (`className` instead of `class`, `frameBorder` instead of `frame-border` etc).
  * `style` HTML attributes are JSON objects and need to be wrapped in `{}`, e.g. `<span style={{"color": "red"}}></span>`.
* `{: ... }` and `{% ... %}` expressions are not supported. Use [components](http://mintlify.com/docs/components) or HTML tags instead.

### Mintlify specifics
* The navigation structure is defined in [docs-mdx/docs.json](docs-mdx/docs.json) and not in the MDX files themselves.
* Pages can be hidden by not including them in [docs-mdx/docs.json](docs-mdx/docs.json) and adding `noindex: true` to the frontmatter. 
  * `make check-lost-pages` build check requires that all pages are either included in [docs-mdx/docs.json](docs-mdx/docs.json) or listed in [hidden_pages.json](hidden_pages.json).
* There's section ToC in the left sidebar and page ToC in the right sidebar. Avoid adding ToC manually.
* Reusable snippets and components are defined in `docs-mdx/snippets/` and can be imported into MDX files.
* All styles and scripts found within [docs-mdx/](docs-mdx) are embedded into all pages, resulting in page bloat. Do not add script and style files unless absolutely necessary. See [here](https://mintlify.com/docs/settings/custom-scripts). There's no control over the order in which they end up on the page.

### AI tools in Mintlify
For AI Mintlify platform generates [.md](https://mintlify.com/docs/ai-ingestion) files and hosts [MCP server](https://mintlify.com/docs/mcp).

### Further references
* [Mintlify](https://mintlify.com) platform documentation:
  * [Page structure](https://mintlify.com/docs/pages)
  * [Navigation](https://mintlify.com/docs/navigation)
  * [Components](https://mintlify.com/docs/components)
  * [Reusable snippets](https://mintlify.com/docs/reusable-snippets)
  * [Custom scripts and styles](https://mintlify.com/docs/settings/custom-scripts)
* [MDX format documentation](https://mdxjs.com/docs/what-is-mdx/)
* [JSX format documentation](https://react.dev/learn/writing-markup-with-jsx) (it's under the hood of MDX)
