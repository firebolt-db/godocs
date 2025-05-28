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
* [x] Fix doc home page design
* [ ] Add /docs-mdx to firebolt-analytics/firebolt-docs-staging
  * [ ] Add the mintlify application to the firebolt-analytics/firebolt-docs-staging repo.
  * [ ] Set up a build check to ensure the /docs-mdx directory is always in sync with the /docs directory in gh-pages branch.
  * [ ] Switch the repo in the mintlify dashboard.
  * [ ] Announce a documentation migration to the team, publish .
  * [ ] Rebase and migrate active branches.
  * [ ] Write HowTo documentation for contributors
  * [ ] Proclaim /docs-mdx as a new source of truth, drop /docs.
* [ ] Shift the domain to mintlify
* [ ] Replace the 307 redirectes for 301 

Nice to have:
* [x] Add preexisting redirects (through old urls is ok)
* [ ] Fix syntax highlighting in query window widgets
* [ ] Enable analytics
* [ ] Output TOC for has_toc index pages (is it needed?)
* [ ] Clean up assets (no unused image copies)
* [ ] Unhide pages hidden in navigation tree for no reason
* [ ] Publish reference pages staying unpublished for no reason
* [ ] Add data type reference page navigation group
