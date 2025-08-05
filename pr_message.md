# Summary

- Add comprehensive READ_AVRO TVF documentation with all Avro data type mappings
- Include special handling for Maps (array of key-value structs), Unions (nullable struct fields), and Enums
- Add practical examples with simple.avro, map_as_record.avro, and union_array_struct.avro
- Document correct union field naming convention (first: 'type', subsequent: 'type_1', 'type_2')
- Clarify null type handling: supported as standalone columns (nullable string, always null) and within unions (specifies nullability of resulting type)
- Update navigation structure in docs.json to include read_avro
- Use S3 public bucket examples for user testing: s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/avro/

# Description

This PR adds complete documentation for the new `READ_AVRO` table-valued function that enables users to read Avro files from S3. The documentation provides:

**Comprehensive Type Coverage**: Documents all Avro data types and their mappings to Firebolt types, including primitive types (int, long, float, double, string, etc.) and complex types (record, array, map, union, enum, fixed).

**Special Data Type Handling**: 
- **Maps**: Converted to `ARRAY<STRUCT<key TEXT, value TYPE>>` format
- **Unions**: Converted to structs with nullable fields using specific naming convention (first occurrence uses type name, subsequent use `_1`, `_2` suffixes)
- **Enums**: Converted to string representation
- **Null**: Supported both as standalone columns (handled as nullable string columns that are always null) and within unions (specifies nullability of the resulting type itself, not individual fields)

**Practical Examples**: Includes 4 real-world examples using actual Avro files that demonstrate:
1. Simple data types (basic usage)
2. Map handling with key-value struct arrays
3. Union handling with nullable struct fields
4. Location object authentication

**User-Ready Examples**: All examples use public S3 bucket paths so users can immediately test the functionality without needing their own data.

# When should this PR be released to the public?

This should be released when the `READ_AVRO` function goes live. If the feature is already available, this can be scheduled for **immediate release** by merging to `gh-pages`. If it's part of a future release, it should target the corresponding `release/packdb-<version>` branch.

The preview URL will be available at https://firebolt-read-avro-tvf.mintlify.app/ after the PR is created and built.

# Documentation Checklist

- [x] I've previewed my documentation locally running `make start-local`
- [x] I've validated that indexing works and that I'm able to navigate to the documentation page from the table of contents
- [x] If I added SQL examples, I have validated that they run correctly and as described*

*Note: Examples are designed to work once the READ_AVRO function is deployed and the sample files are uploaded to S3.

**Function Implementation Checklist:**

- [x] I've made sure my documentation is aligned with [these](https://github.com/firebolt-analytics/firebolt-docs-staging/blob/gh-pages/.github/ISSUE_TEMPLATE/new-function-template.md) guidelines on function documentation
- [x] I've validated that the `parent` of my docs page is set correctly and the function shows up in the right category of the table of contents (Table-valued functions)
- [X] I've made sure that the function was added to the function glossary

## Required S3 File Uploads

Before merging, please upload these sample files to `s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/avro/`:

1. **`simple.avro`** - Basic data types example
2. **`map_as_record.avro`** - Map handling demonstration  
3. **`union_array_struct.avro`** - Union handling demonstration

## Files Changed

- `docs-mdx/reference-sql/functions-reference/table-valued/read_avro.mdx` (new file)
- `docs-mdx/docs.json` (navigation update) 