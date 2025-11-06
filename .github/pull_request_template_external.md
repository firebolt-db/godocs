PR title should follow [Firebolt PR convention](https://packboard.atlassian.net/wiki/spaces/PACB/pages/3854237702/Firebolt+PR+Convention).
Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test.

Choose from one of the types above and set PR title to match `type[(scope)]: what changed (FIR-XXX)` format.

# Description
Please include a summary of the change and which issue is fixed. Please also include relevant motivation and context.

# When should this PR be released to the public?
If the feature is live, the docs can be scheduled for **immediate release** by filing the PR to the gh-pages branch.
If it's part of a **future release**, please file the PR against the corresponding release/packdb-<version> branch. 

# Documentation Checklist
- [ ] I've previewed my documentation locally running `make start-local` (or using [this](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) tutorial) 
- [ ] I've validated that indexing works and that I'm able to navigate to the documentation page from the table of contents
- [ ] If I added SQL examples, I have validated that they run correctly and as described. 

If this PR touches a function implementation (aggregate, scalar, or table-valued):
- [ ] I've made sure my documentation is aligned with [these](https://github.com/firebolt-db/godocs/blob/gh-pages/.github/ISSUE_TEMPLATE/new-function-template.md) guidelines on function documentation 
- [ ] I've validated that the `parent` of my docs page is set correctly and the function shows up in the right category of the table of contents
- [ ] I've made sure that the function was added to the function glossary
