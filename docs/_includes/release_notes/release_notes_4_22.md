## Firebolt Release Notes - Version 4.22

### New Features

<!-- Auto Generated Markdown for FIR-46137 - Owned by Jonathan Doron -->
**Added the `ICU_NORMALIZE` function to standardize text formats across locales

**
Added the `ICU_NORMALIZE` function to process text based on a specific locale. This helps in standardizing text formats across different languages and regions, ensuring uniformity and compatibility in data outputs.


<!-- Auto Generated Markdown for FIR-27532 - Owned by Arsenii Krasikov -->
**Added the `AGO(interval)` function for subtracting intervals from the current timestamp. 

**
Added the `AGO(interval)` function, which subtracts the specified interval from the current timestamp. This addition provides users with a convenient way to calculate past dates and times, enhancing time-based data analysis.
Documentation for the function is available [here]({% link sql_reference/functions-reference/date-and-time/ago.md %}).


<!-- Auto Generated Markdown for FIR-45210 - Owned by Arsenii Krasikov -->
**Added a named parameter `INFER_SCHEMA` to the `READ_CSV` function for improved data processing accuracy and efficiency

**
- Added a named parameter `INFER_SCHEMA` to the `READ_CSV` function. When `INFER_SCHEMA` is true, the function determines column data types instead of using `TEXT`. This enhancement improves data processing accuracy and efficiency.


<!-- Auto Generated Markdown for FIR-37504 - Owned by Cosmin Cosmin Pop -->
**Introduced a new flow for managing service accounts with enhanced security via improved secret rotation and user associations in any organization account  

**
Introduced a new flow for creating and altering service accounts that enables user associations in any organization account. This improvement simplifies account management and enhances security through an improved process for rotating secrets.


### Behavior Changes

<!-- Auto Generated Markdown for FIR-46028 - Owned by Pascal Schulze -->
**Made columns in `information_schema.accounts`, `information_schema.engines`, and `information_schema.users` nullable

**
The columns in `information_schema.accounts`, `information_schema.engines`, and `information_schema.users` are now nullable. This change allows for more flexible handling of data across these schemas.


### Performance Improvements

<!-- Auto Generated Markdown for FIR-44352 - Owned by Lorenz Hübschle -->
**Rearchitected the Parquet reader for predictable memory usage and improved performance with external tables and `READ_PARQUET` function.**
The Parquet reader was rearchitected to provide more predictable memory usage when reading from external tables or using the `READ_PARQUET` table-valued function. This change improves performance for many Parquet workloads. Users benefit from enhanced memory efficiency and faster query processing. More updates, like applying these changes to the `COPY FROM` command, are planned for future releases.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-46431 - Owned by Lorenz Hübschle -->
**Fixed incorrect results from multi-node engines when using `UNION ALL` with overlapping aggregation or join keys followed by further aggregation or joining

**
Resolved an issue that caused incorrect results on multi-node engines. This occurred when performing a `UNION ALL` over subqueries with overlapping but separate aggregation or join keys, followed by further aggregation or joining on those keys. This fix enhances data accuracy in complex query operations.
