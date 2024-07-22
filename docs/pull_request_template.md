If you're adding a new SQL function (aggregate, scalar, or table-valued), check [this](https://github.com/firebolt-analytics/firebolt-docs-staging/blob/gh-pages/.github/ISSUE_TEMPLATE/new-function-template.md) link providing guidelines on what information we're interested in including in docs :
Then go over the following steps :
- [ ] Preview your documentation locally running `make start-local` (or using [this](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) tutorial) 
- [ ] Validate that indexing works and that you’re able to navigate to the documentation page from the table of contents
- [ ] Make sure that the function was added to the function glossary
Note that the first step will be needed only until we have preview automation in the CI

For other changes (not SQL functions additions) follow those steps:
- [ ] Preview your documentation locally running `make start-local` (or using [this](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) tutorial) 
- [ ] Validate  that indexing works and that you're able to navigate to the documentation page from the table of contents
Note that the first step will be needed only until we have preview automation in the CI
