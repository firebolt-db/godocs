# Firebolt Release Notes - Version 4.13

### Behavior Changes

<!-- FIR-37266 - Owned by Mariia Kaplun -->
**Removed secured objects from `information_schema` views**

Users can now only access information about objects for which they have the appropriate permissions or ownership for in [information_schema views]({% link sql_reference/information-schema/views.md %}).

### New Features

<!-- Auto Generated Markdown for FIR-42091 - Owned by Tal Zelig -->
**`GRANT ALL ON ACCOUNT` and `REVOKE ALL ON ACCOUNT` statements for role-based privileges**    
The statements `GRANT ALL ON ACCOUNT account_name TO role_name` and `REVOKE ALL ON ACCOUNT account_name FROM role_name` are now supported. They grant or revoke all account-related privileges to the specified role `role_name`.

<!-- Auto Generated Markdown for FIR-42324 - Owned by David Boublil -->
**Support for nested arrays in Parquet files**
We can now ingest Parquet files with a nested array structure of arbitrary depth, e.g., array(array(array(string))).

### Bug Fixes

<!-- Auto Generated Markdown for FIR-42575 - Owned by Tal Zelig -->
**`@` character support restored in usernames**     
The usage of character `@` is allowed in usernames again, which was previously restricted. The following statements are now valid and will not cause errors.

```
CREATE USER "ex@mple";
ALTER USER user_name RENAME TO "ex@mple";
```

<!-- Auto Generated Markdown for FIR-38781 - Owned by jingtao.huang -->
**Resolved memory overuse during CSV import with large rows**    
Resolved a memory overconsumption problem that occurred when importing CSV files with large rows into existing tables.

<!-- Auto Generated Markdown for FIR-42413 - Owned by Jonathan Doron -->
**Resolved `explain vacuum` and `explain` to improve error handling and result accuracy**    
The behavior of `explain vacuum` has been updated to:

1. Display an accurate error message when a table has already been vacuumed.
2. Return non-empty results when running `explain vacuum` on an AI.

Additionally, `explain` has been updated to show an error if the specified relation does not exist.
