# Moving and Reorganizing Documentation Pages

Guide for safely moving pages and maintaining URL redirects.

## Overview

Moving pages requires careful coordination of file moves, navigation updates, and redirect configuration to ensure users can still access content at old URLs.

## Before You Start

### Check Current Usage

1. **Check external links**: Search for external sites linking to the page
2. **Verify internal references**: Find all internal links that need updating

### Plan Your Move

- Decide on the new location and URL structure
- Plan redirect strategy for old URLs
- Consider impact on navigation hierarchy

## Step-by-Step Process

### 1. Move the File

Move your MDX file to the new location:

```bash
# Example: Moving a SQL function from one category to another
mv docs-mdx/reference-sql/functions-reference/string/upper.mdx \
   docs-mdx/reference-sql/functions-reference/text/upper.mdx
```

### 2. Update Navigation Structure

Update `docs-mdx/docs.json` to reflect the new location:

```json
{
  "group": "Text Functions",
  "pages": [
    "reference-sql/functions-reference/text/upper",
    "reference-sql/functions-reference/text/lower"
  ]
}
```

Remove the page from its old location in the navigation.

### 3. Add Redirects

Add redirect entries to `docs-mdx/docs.json` in the `redirects` section:

```json
{
  "redirects": [
    {
      "source": "/reference-sql/functions-reference/string/upper",
      "destination": "/reference-sql/functions-reference/text/upper",
      "permanent": true
    }
  ]
}
```

**Important**: Use `"permanent": true` for SEO-friendly 301 redirects.

**⚠️ Warning about Permanent Redirects**: Setting `"permanent": true` creates a 301 redirect that tells search engines and browsers to permanently cache the redirect. Only use this when you're certain the page move is final. If you might need to change the redirect later, consider using `"permanent": false` initially and switching to `true` after confirming the move is working correctly. Premature permanent redirects can cause confusion and caching issues that are difficult to resolve.

### 4. Update Internal Links

Find and update all internal references to the moved page:

```bash
# Search for references to the old path
grep -r "reference-sql/functions-reference/string/upper" docs-mdx/

# Update found references to use the new path
```

### 5. Update Cross-References

Check for any cross-references in related pages:
- Function overview pages
- Category index pages  
- Related function lists
- Tutorial examples

### 6. Validate Changes

Run comprehensive validation:

```bash
# Check navigation structure
make check-navigation

# Validate redirects
make check-lost-redirects

# Check for broken links
make check-links

# Run all validations
make check-all
```

## Advanced Scenarios

### Moving Multiple Related Pages

When moving a group of related pages:

1. **Plan the structure**: Design the new hierarchy first
2. **Move in batches**: Group related moves together
3. **Update navigation**: Restructure navigation sections as needed
4. **Bulk redirects**: Add redirects for all moved pages

### Renaming Categories

When renaming entire categories:

1. **Create new directory structure**
2. **Move all files** to new locations
3. **Update navigation** with new category names
4. **Add category-level redirects** for old paths
5. **Update all cross-references**

### URL Slug Changes

When changing URL slugs (file names):

```bash
# Example: Renaming for better SEO
mv docs-mdx/guides/data-loading/copy-from.mdx \
   docs-mdx/guides/data-loading/loading-data-from-s3.mdx
```

Ensure redirects cover both the old file name and any intermediate URLs.

## Registry File Updates

### Known Pages Registry

The system automatically updates `known_pages.json` to track the new URLs. You can manually regenerate it:

```bash
make check-lost-redirects-regenerate
```

### Hidden Pages

If temporarily hiding moved pages during reorganization, add them to `hidden_pages.json`:

```json
{
  "path": "path/to/moved-page.mdx", 
  "reason": "temporarily hidden during reorganization"
}
```

## Testing Your Changes

### Local Testing

1. **Start development server**: `make start-local`
2. **Test old URLs**: Verify redirects work correctly
3. **Test new URLs**: Ensure pages load at new locations
4. **Check navigation**: Verify pages appear in correct sections

### Validation Testing

```bash
# Test redirect validation
make check-redirect-loops

# Test for lost pages
make check-lost-pages

# Comprehensive validation
make check-all
```

## Best Practices

### URL Design

- **Use descriptive paths**: Make URLs self-explanatory
- **Follow hierarchy**: Reflect content organization in URL structure
- **Avoid deep nesting**: Keep URLs reasonably short
- **Use consistent naming**: Follow existing conventions

### Redirect Strategy

- **Always add redirects**: Never break existing URLs
- **Use permanent redirects**: Set `"permanent": true` for moved content
- **Test thoroughly**: Verify redirects work as expected
- **Monitor analytics**: Track redirect usage over time

### Communication

- **Document changes**: Note moves in pull request descriptions
- **Notify stakeholders**: Alert teams that reference moved content
- **Update external docs**: Inform partners of URL changes

## Troubleshooting

### Common Issues

- **Redirect loops**: Check for circular redirects in validation
- **Lost pages**: Ensure moved pages are in navigation or hidden_pages.json
- **Broken links**: Update all internal references to moved pages
- **Navigation errors**: Verify new paths match file locations exactly

### Recovery Steps

If something goes wrong:

1. **Revert file moves**: Move files back to original locations
2. **Restore navigation**: Revert docs.json changes
3. **Remove redirects**: Clean up any problematic redirects
4. **Re-validate**: Run validation suite to confirm fixes

## Next Steps

After moving pages:
1. Create a pull request with all changes
2. Monitor CI/CD validation results
3. Test redirects in the deployed environment
4. Update any external documentation or bookmarks
5. Monitor analytics for redirect usage patterns
