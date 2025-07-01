This repository contains the source code for the Firebolt documentation, which is built using MDX and Mintlify.

<!-- TOC -->
  * [HOWTO](#howto)
    * [How to add a new page](#how-to-add-a-new-page)
    * [How to move an existing page](#how-to-move-an-existing-page)
    * [How to add an interactive SQL example](#how-to-add-an-interactive-sql-example)
    * [How to preview locally](#how-to-preview-locally)
    * [How to preview remotely](#how-to-preview-remotely)
    * [How to release changes](#how-to-release-changes)
  * [Repository structure](#repository-structure)
    * [Local checks](#local-checks)
      * [Merge conflict markers](#merge-conflict-markers)
      * [Navigation structure](#navigation-structure)
      * [Internal link validation](#internal-link-validation)
      * [External link validation](#external-link-validation)
      * [SQL example check](#sql-example-check)
    * [GitHub Workflow Validation](#github-workflow-validation)
  * [MDX format](#mdx-format)
    * [How it's different from Markdown](#how-its-different-from-markdown)
    * [Mintlify specifics](#mintlify-specifics)
<!-- TOC -->

## HOWTO
### How to add a new page
1. Before you start
   1. Read the [MDX format](#mdx-format) section below.
   2. See the example page at [function-template.mdx](function-template.mdx).
2. Create the MDX file in the appropriate directory under `docs-mdx/`. **No whitespace or upper case is allowed in the path.**
3. Consider adding [keywords](https://mintlify.com/docs/pages#internal-search-optimization) and [description](https://mintlify.com/docs/pages#descriptions) to the frontmatter of the page for better internal SEO.
4. Add the file to the navigation structure in `docs-mdx/docs.json`. **The navigation structure must reflect the directory structure.**
5. Run the checks (`make check-all` or `make`) to ensure everything is correct and update the `known_pages.json` file with the new URL.
6. Preview the page locally using `make start-local`.
7. Push the changes to the repository.
8. Preview the results remotely (see [How to preview the result remotely](#how-to-preview-remotely)).
9. See the [release workflow](#how-to-release-changes) section for how to release the changes.

### How to move an existing page
NB: `mint rename` does a terrible job, do not use it.

1. Move the MDX file to the new location in `docs-mdx/`. **No whitespace or upper case is allowed in the path.**
2. Update all cross-references to the page in other MDX files.
3. Update the navigation structure in `docs-mdx/docs.json` with the new location. **The navigation structure must reflect the directory structure.**
4. Run `make check-links` and `make check-links-using-crawler` to find missed links.
5. Add a redirect from the old URL to the new URL in `docs-mdx/docs.json`.
6. Run the checks (`make check-all` or `make`) to ensure everything is correct and update the `known_pages.json` file with the new URL.
7. Preview the new navigational structure locally using `make start-local`.
8. Push the changes to the repository.
9. Preview the results remotely (see [How to preview the result remotely](#how-to-preview-remotely)).
10. See the [release workflow](#how-to-release-changes) section for how to release the changes.

### How to add an interactive SQL example
We have interactive examples in the documentation. These run against a Firebolt docs server.
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
5. Push the changes to the repository.
6. Preview the results remotely (see [How to preview the result remotely](#how-to-preview-remotely)).
7. See the [Release workflow](#how-to-release-changes) section for how to release the changes.

### How to preview locally
1. Run `make start-local`
2. Open http://localhost:3000/ in your browser to preview the documentation.

### How to preview remotely
1. Open a pull request in the repository.
2. Wait for the CI/CD pipeline to run. This will build the documentation and deploy it to a remote preview environment.
3. Go to `https://firebolt-[your-branch-name-with-dashes].mintlify.app/` to see the remote preview of your changes. E.g., if your branch is `my_feature/new-page`, the URL will be `https://firebolt-my_feature-new-page.mintlify.app/`.

### How to release changes
**TODO**

## Repository structure
* `docs-mdx/` contains all the MDX files for the documentation:
  * `docs-mdx/docs.json` defines the navigation structure of the documentation.
  * `docs-mdx/assets/` contains static assets like images, styles and scripts used in the documentation. All styles and scripts are embedded in the MDX files by mintlify. See [here](https://mintlify.com/docs/settings/custom-scripts). There's no control over their order on the page.
  * `docs-mdx/snippets/` contains reusable [snippets](https://mintlify.com/docs/reusable-snippets) and [components](https://mintlify.com/docs/react-components).
* `scripts/` contains checking scripts and utilities:
  * `scripts/check_group_structure.py` checks that the pages in `docs.json` are organized into consistent groups and directory structure mirrors the navigational structure.
  * `scripts/check_lost_pages.py` checks that all MDX files are referenced in `docs.json` unless they are listed in `hidden_pages.json`.
  * `scripts/check_redirect_loops.py` checks that there are no circular redirects in the documentation.
  * `scripts/check_lost_redirects.py` checks that all previously known URLs (listed `known_pages.json`) either have a corresponding page or a proper redirect.
  * `scripts/check_sql_examples.py` checks that pre-generated results in `<QueryWindow/>` components are the same as the real results.
  * `scripts/check_merge_conflict_markers.sh` checks that there are no Git merge conflict markers in the documentation files.
* `hidden_pages.json` contains all pages that are intentionally not included in the navigation. This is to prevent accidental hiding of pages by forgeting to add them to `docs.json`.
* `known_pages.json` contains all URLs that have ever existed in the documentation. This is used to check for lost redirects.
* `function-template.mdx` is an example page.

### Local checks
All local checks can be run with `make check-all` or just `make`

#### Merge conflict markers
`make check-markers` to scan all files for Git merge conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

#### Navigation structure
`make check-navigation` to check the navigation structure.
`make check-navigation-regenerate` to check the navigation structure and regenerate `known_pages.json`.

Includes the following checks:
- **Group Structure**: Validates that pages in docs.json follow proper hierarchical organization
- **Lost Pages**: Identifies MDX files not referenced in navigation or `hidden_pages.json`
- **Redirect Loops**: Detects circular redirects that would break navigation.
- **Lost Redirects**: Ensures all previously known URLs in `known_pages.json` have proper redirects. Also checks that all urls are present in `known_pages.json`.

#### Internal link validation
`make check-internal-links` to run Mintlify's built-in broken link checker and validate internal links in the documentation.

#### External link validation
`make check-links-using-crawler` to bring up a local site instance using `mint dev` and run [muffet](https://github.com/raviqqe/muffet) link crawler against it.

#### SQL example check
* `make check-sql` to check that all `<QueryWindow/>` components when run against live Firebolt staging API produce expected results.
* `make package-docs` to regenerate all results for all `<QueryWindow/>` components in the documentation.
* `make package-missing-docs` to generate results for all `<QueryWindow/>` components that don't have pre-generated results.

### GitHub Workflow Validation

The `.github/workflows/pr-check.yml` workflow runs four parallel jobs on every pull request:

* **check-basic-errors**: Merge conflict markers, legacy directory checks, navigation validation
* **check-broken-links**: Internal link validation using Mintlify
* **check-links-using-crawler**: External link validation (informational, doesn't block merge)
* **check-sql-examples**: SQL example validation (informational, doesn't block merge)

Each job posts its status in the status comment on the PR and adds detailed error information if validation fails.

## MDX format
* Mintlify platform documentation:
  * [Page structure](https://mintlify.com/docs/pages)
  * [Navigation](https://mintlify.com/docs/navigation)
  * [Components](https://mintlify.com/docs/components)
  * [Reusable snippets](https://mintlify.com/docs/reusable-snippets)
  * [Custom scripts and styles](https://mintlify.com/docs/settings/custom-scripts)
* [MDX format documentation](https://mdxjs.com/docs/what-is-mdx/)
* [JSX format documentation](https://react.dev/learn/writing-markup-with-jsx) (it's under the hood of MDX)

### How it's different from Markdown
* `{: ... }` and `{% ... %}` expressions are not supported. Use [components](http://mintlify.com/docs/components) or HTML tags instead.
* MDX is JSX-based, meaning:
  * Each page is a React component.
  * All tags are React components. Yes, HTML tags too.
  * HTML tags need to be closed and lowercase.
  * Attributes are camel case (`className` instead of `class`, `frameBorder` instead of `frame-border` etc).
  * `style` attributes are JSON objects and need to be wrapped in `{}`, e.g. `style={{"color": "red"}}`.
  * Some HTML tags are not supported.
  * Pages won't compile if there's any JSX syntax error. Use `make start-local` or `make check-links` to see errors.
* The markup syntax is stricter than Markdown, especially for tables. Preview the result [locally](#how-to-preview-locally) or [remotely](#how-to-preview-remotely) to see how it actually renders.

### Mintlify specifics
* The navigation structure is defined in `docs-mdx/docs.json` and not in the MDX files themselves.
* Pages can be hidden by not including them in `docs-mdx/docs.json` and adding `noindex: true` to the frontmatter. 
  * `make check-lost-pages` build check requires that all pages are either included in `docs.json` or listed in `hidden_pages.json`.
* H1 headers look out of place because each page has its title rendered as a H1 header at the top.
* No automatic ToC to embed on page. There's section ToC in the left sidebar and page ToC in the right sidebar.
* The platform generates `.md` files and hosts [MCP server](https://mintlify.com/docs/mcp) for [AI](https://mintlify.com/docs/ai-ingestion).
* Reusable snippets and components are defined in `docs-mdx/snippets/` and can be imported into MDX files.
* All styles and scripts within `docs-mdx/` are embedded into all pages. See [here](https://mintlify.com/docs/settings/custom-scripts).
  * There's no control over the order in which they end up on the page.
* Rendered pages are very heavy in Javascript and may be slow.
