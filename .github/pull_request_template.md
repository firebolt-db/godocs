# Description
Please include a summary of the change and which issue is fixed. Please also include relevant motivation and context.

{:note}
# When should this PR be released to the public?
You can request an **immediate release** to the public docs if the feature is live.
If it's part of a **future release**, please specify which release it should be released with. 
<BR>
Ex: Packdb 4.4, estimated release to public: 8/28/24.

# Documentation Checklist
- [ ] I've previewed my documentation locally running `make start-local` (or using [this](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) tutorial) 
- [ ] I've validated that indexing works and that I'm able to navigate to the documentation page from the table of contents

If this PR touches a function implementation (aggregate, scalar, or table-valued):
- [ ] I've made sure my documentation is aligned with [these](https://github.com/firebolt-analytics/firebolt-docs-staging/blob/gh-pages/.github/ISSUE_TEMPLATE/new-function-template.md) guidelines on function documentation 
- [ ] I've validated that the `parent` of my docs page is set correctly and the function shows up in the right category of the table of contents
- [ ] I've made sure that the function was added to the function glossary

