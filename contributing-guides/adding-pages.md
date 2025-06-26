# Adding New Documentation Pages

Step-by-step guide for adding new pages to Firebolt documentation.

## Prerequisites

- Repository cloned locally
- Python 3.10+ installed
- Node.js and npm installed for Mintlify

## Step-by-Step Process

### 1. Create the MDX File

Create your new page in the appropriate directory under `docs-mdx/`:

```bash
# For SQL reference documentation
docs-mdx/reference-sql/[category]/your-page.mdx

# For user guides  
docs-mdx/guides/[category]/your-page.mdx

# For API reference
docs-mdx/reference-api/your-page.mdx
```

### 2. Add Frontmatter

Every MDX file must include frontmatter with at least a title. You can also specify a custom sidebar title:

```mdx
---
title: Your Page Title
description: Brief description of the page content
sidebarTitle: Custom Sidebar Title (optional)
---

Your content here...
```

### 3. Update Navigation Structure

Add your page to the navigation in `docs-mdx/docs.json`:

```json
{
  "group": "Your Category",
  "pages": [
    "existing-page",
    "your-new-page"
  ]
}
```

**Important**: Use the file path relative to `docs-mdx/` without the `.mdx` extension.

### 4. Validate Your Changes

Run the validation suite to ensure everything is correct:

```bash
# Check navigation structure
make check-navigation

# Check for broken links
make check-links

# Run all validations
make check-all
```

### 5. Test Locally

Start the local development server to preview your changes:

```bash
make start-local
```

Navigate to `http://localhost:3000` to see your new page.

## Common Issues and Solutions

### Page Not Appearing in Navigation

- Verify the path in `docs.json` matches your file location exactly
- Ensure you're using the path relative to `docs-mdx/` without `.mdx` extension
- Check that your file is in the correct directory structure

### Validation Errors

- **Lost Pages Error**: Your page exists but isn't in navigation - add it to `docs.json` or `hidden_pages.json`
- **Group Structure Error**: Your page doesn't follow the expected directory hierarchy
- **Broken Links**: Fix any internal links that point to non-existent pages

### Hidden Pages

If your page should exist but not appear in navigation (e.g., work in progress), add it to `hidden_pages.json`:

```json
{
  "path": "path/to/your-page.mdx",
  "reason": "work in progress - will be released in version X.Y"
}
```

## Best Practices

- Follow the [Google Style Guide](https://developers.google.com/style) for writing
- Use descriptive, SEO-friendly titles
- Include relevant cross-references to related pages
- Test all code examples before publishing
- Keep file names lowercase with hyphens (kebab-case)

## Next Steps

After adding your page:
1. Create a pull request with your changes
2. The CI/CD pipeline will automatically validate your changes
3. Address any validation failures reported in PR comments
4. Request review from the documentation team
