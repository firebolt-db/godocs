* [x] Existing content works
  * [x] own tests pass (same md, no markup left)
  * [x] urls are beautiful - also prevent old redirects from causing infinite loops
  * [x] mint compiler accepts
  * [x] mint link check accepts 
  * [x] navigation tree works
  * [x] icon images stay inline
  * [x] fixed style attribute in jsx https://react.dev/errors/62?invariant=62
  * [x] fixed nonrendering figure tag images
  * [x] fixed page layout being too narrow for examples
  * [x] old urls redirect to new urls
  * [x] all includes work
  * [x] home page design is neat
  * [x] home page design is neat on small screens
* [ ] Add /docs-mdx to firebolt-analytics/firebolt-docs-staging
  * [x] Add the mintlify application to the firebolt-analytics/firebolt-docs-staging repo.
  * [x] Switch the repo in the mintlify dashboard.
  * [x] Set up a build check to ensure the /docs-mdx directory is always in sync with the /docs directory in gh-pages branch.
  * [x] Migrate the SQL example check.
  * [x] Announce the documentation migration to the team.
  * [x] Allow authoring new documentation in mdx
  * [x] Rebase and migrate active branches:
    * [x] release/packdb-4.22
    * [x] performance_and_observability
    * [x] jingtao/iceberg_4_22
    * [x] release_notes_4_22
    * [x] firebolt-core
    * [x] fix-billing-pages
  * [x] Update the [release notes writer](https://github.com/firebolt-analytics/release-process/blob/main/release_notes_writer.py) to make the proper changes.
  * [x] Proclaim /docs-mdx as a new source of truth, drop /docs.
* [x] Shift the domain to mintlify
  * [x] Test domain shift on auxiliary domain
  * [x] Disable telemetry to not to be blocked by cookie consent
* [x] Add preexisting redirects (through old urls is ok)

Nice to have:
* [ ] Enable analytics
  * [ ] Integrate with cookie consent platform
* [ ] Replace the 307 redirectes for 301
* [ ] Check that most of the pages are fit for small screens
* [ ] Check documentation for inconsistencies in formatting
* [ ] Write HowTo documentation for contributors.
* [ ] Fix syntax highlighting in query window widgets
* [ ] Unhide pages hidden in navigation tree for no reason
* [ ] Publish reference pages staying unpublished for no reason
  * [ ] Add data type reference page navigation group and data type pages with "Details on " prefix
  * [ ] Add interactive examples where they work but not included
  * [ ] Clean up assets (no unused image copies)
* [ ] Fix statistical examples
* [ ] Output TOC for has_toc index pages where needed
* [ ] Fix screenshots for dark mode
