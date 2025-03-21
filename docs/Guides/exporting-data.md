---
redirect_from:
  - /exporting-query-results.html
layout: default
title: Export data
parent: Guides
nav_order: 10
---

# Export data
Firebolt allows you to export data from a `SELECT` query directly to an Amazon S3 location using the `COPY TO` statement.  
This method is more flexible and efficient than manual exports from the SQL workspace, making it ideal for **data sharing, integration, and archival**.

For more information, see [COPY TO](../sql_reference/commands/data-management/copy-to.md).

## How to Export Data
To export data from Firebolt, use the `COPY TO` statement in the following format:

```sql
COPY (
    SELECT column1, column2 FROM my_table WHERE condition
) 
TO 's3://your-bucket/path/'
WITH (FORMAT = 'CSV')
CREDENTIALS = ('aws_key_id'='your-key' 'aws_secret_key'='your-secret');
```

## Examples

### Example 1: Exporting Data in CSV Format
Use CSV when you need a simple, widely supported format for spreadsheets, relational databases, or data exchange.
```sql
COPY (SELECT user_id, event_type, timestamp FROM user_events) 
TO 's3://my-export-bucket/user_events.csv'
WITH (FORMAT = 'CSV', HEADER = TRUE)
CREDENTIALS = ('aws_key_id'='your-key' 'aws_secret_key'='your-secret');
```

### Example 2: Exporting Data in Parquet Format
Parquet is best for big data workloads, as it offers compressed, columnar storage optimized for analytics and query performance.
```sql
COPY (SELECT * FROM sales_data) 
TO 's3://my-export-bucket/sales_data.parquet'
WITH (FORMAT = 'PARQUET')
CREDENTIALS = ('aws_key_id'='your-key' 'aws_secret_key'='your-secret');
```

### Example 3: Exporting Data in JSON Format
JSON is ideal for APIs, web applications, and NoSQL databases, as it supports nested and flexible data structures.
```sql
COPY (SELECT order_id, order_details FROM orders) 
TO 's3://my-export-bucket/orders.json'
WITH (FORMAT = 'JSON')
CREDENTIALS = ('aws_key_id'='your-key' 'aws_secret_key'='your-secret');
```

### Example 4: Exporting Data in TSV Format
TSV is similar to CSV but uses tab delimiters, making it useful for structured text data that may contain commas.
```sql
COPY (SELECT name, age, city FROM customers) 
TO 's3://my-export-bucket/customers.tsv'
WITH (FORMAT = 'TSV')
CREDENTIALS = ('aws_key_id'='your-key' 'aws_secret_key'='your-secret');
```

## Choosing the Right Export Format
| Format                     | Best For                                  | Characteristics                                  |
|---------------------------|-------------------------------------------|--------------------------------------------------|
| **CSV (Comma-Separated)** | General data exchange, spreadsheets, SQL  | Simple, widely supported, easy to read           |
| **TSV (Tab-Separated)**   | Structured text data                      | Like CSV, but uses tab instead of comma          |
| **JSON**                  | APIs, web applications, NoSQL databases   | Flexible, human-readable, supports nested data   |
| **PARQUET**               | Big data processing, analytics workloads  | Compressed, columnar, optimized for querying     |

### Which Format Should You Use?
- **CSV/TSV** → Best for Excel, databases, or general data exchange  
- **JSON** → Best for web apps, APIs, or NoSQL integrations  
- **PARQUET** → Ideal for analytics and performance-sensitive workloads 

## Additional Considerations
### Performance Tips
- Use **PARQUET** for large datasets for better compression and query speed  
- Export only required columns and use filters to reduce data volume  
- Ensure proper permissions are set on your S3 bucket  

### Security & Credentials
- Always use **secure AWS credentials**  
- Prefer **IAM roles** over hardcoded credentials for better security  

## Next Steps
For advanced options like **compression**, **partitioning**, and **null handling**, refer to the [COPY TO](../sql_reference/commands/data-management/copy-to.md).

