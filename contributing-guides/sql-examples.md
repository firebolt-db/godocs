# Adding and Updating SQL Examples

Guide for working with interactive SQL examples in Firebolt documentation.

## Overview

Firebolt documentation uses interactive SQL examples that run against a live staging environment. These examples are validated automatically to ensure accuracy.

## Adding a New SQL Example

### 1. Import QueryWindow Component

Add the import at the top of your MDX file if not already present:

```mdx
import {QueryWindow} from '/snippets/query-window.mdx';
```

### 2. Add QueryWindow Component

Insert the component where you want the example to appear:

```mdx
<QueryWindow content={{
  "sql": "SELECT ABS(-200.50) as result;",
  "result": {
    "data": [
      [200.5]
    ],
    "meta": [
      {
        "name": "result", 
        "type": "double"
      }
    ],
    "query": {
      "query_id": "7eab6ce7-0174-4e01-adee-2765f715d70a",
      "query_label": null,
      "request_id": "02476fa1-b9ae-4ece-9606-84cee56a595b"
    },
    "rows": 1,
    "statistics": {
      "bytes_read": 1,
      "elapsed": 0.009298,
      "rows_read": 1,
      "scanned_bytes_cache": 0,
      "scanned_bytes_storage": 0,
      "time_before_execution": 0.00025336,
      "time_to_execute": 9.5656e-05
    }
  }
}} />
```

### 3. Generate Results Automatically

You can leave the `result` field empty and generate it automatically:

```mdx
<QueryWindow content={{
  "sql": "SELECT CURRENT_DATE() as today;",
  "result": {}
}} />
```

Then run:

```bash
# Generate results for all missing examples
make package-missing-docs

# Or generate only for examples without results
make package-docs
```

## Updating Existing SQL Examples

### 1. Modify the SQL

Update the `sql` field in the QueryWindow component:

```mdx
<QueryWindow content={{
  "sql": "SELECT UPPER('hello world') as greeting;",
  "result": {
    // existing result data...
  }
}} />
```

### 2. Regenerate Results

After changing SQL, regenerate the expected results:

```bash
make package-docs
```

This will execute your updated SQL against the staging environment and update the result data.

### 3. Validate Changes

Run validation to ensure your examples work correctly:

```bash
make check-sql
```

## SQL Example Best Practices

### Writing Good SQL Examples

- **Keep it simple**: Use clear, focused examples that demonstrate one concept
- **Use realistic data**: Examples should reflect real-world usage patterns  
- **Include context**: Explain what the example demonstrates
- **Test thoroughly**: Ensure examples work in the staging environment

### Handling Dynamic Results

Some SQL functions return dynamic values that change on each execution:

#### Random Values
```sql
SELECT RANDOM() as random_number;
```
The validation system automatically redacts random values.

#### UUIDs
```sql
SELECT GEN_RANDOM_UUID_TEXT() as uuid;
```
UUID values are automatically redacted during validation.

#### Timestamps
```sql
SELECT CURRENT_TIMESTAMP() as now;
```
Consider using fixed timestamps in examples for consistency.

### Error Handling

If your SQL example produces an error:

1. **Intended errors**: Include the error in your result for educational purposes
2. **Unintended errors**: Fix the SQL or check staging environment access
3. **Environment issues**: Contact the documentation team

## Validation Process

### Automatic Validation

The validation system:
1. Extracts SQL from QueryWindow components
2. Executes queries against `https://api.staging.firebolt.io/demo/execute-query`
3. Compares actual results with expected results
4. Normalizes dynamic values (UUIDs, random numbers, timing data)
5. Reports any mismatches

### Manual Validation

Test your examples locally:

```bash
# Validate specific files
echo "path/to/your/file.mdx" | make check-sql

# Validate all examples (quiet mode)
make check-sql
```

## Troubleshooting

### Common Issues

- **API timeout**: Staging environment may be slow - try again later
- **Permission errors**: Ensure staging environment access is configured
- **Result mismatch**: SQL may have changed behavior - regenerate results
- **Syntax errors**: Validate SQL syntax before adding to documentation

### Getting Help

- Check the staging environment status
- Review recent changes to SQL functions
- Contact the documentation team for environment issues
- Use the `#documentation` Slack channel for questions

## Next Steps

After adding or updating SQL examples:
1. Run local validation with `make check-sql`
2. Test in local development server with `make start-local`
3. Create a pull request
4. Monitor CI/CD validation results
5. Address any failures reported in PR comments
