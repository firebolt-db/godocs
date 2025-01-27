# Firebolt Release Notes - Version 4.13

### New Features

<!-- Auto Generated Markdown for FIR-42091 - Owned by Tal Zelig -->
**`GRANT ALL ON ACCOUNT` and `REVOKE ALL ON ACCOUNT` statements for role-based privileges**    
The statements `GRANT ALL ON ACCOUNT account_name TO role_name` and `REVOKE ALL ON ACCOUNT account_name FROM role_name` are now supported. They grant or revoke all account-related privileges to the specified role `role_name`.

<!-- Auto Generated Markdown for FIR-42324 - Owned by David Boublil -->
**Support for Nested Arrays in Parquet Files**
You can now ingest Parquet files containing nested array structures at any depth. For example: array(array(array(string))).

### Behavior Changes

<!-- FIR-37266 - Owned by Mariia Kaplun -->
**Removed secured objects from `information_schema` views**

Users can now only access information about objects for which they have the appropriate permissions or ownership for in [information_schema views]({% link sql_reference/information-schema/views.md %}).

### Bug Fixes

<!-- Auto Generated Markdown for FIR-42575 - Owned by Tal Zelig -->
**`@` character support restored in usernames**     
The usage of character `@` is allowed in usernames again, which was previously restricted. The following statements are now valid and will not cause errors.

```
CREATE USER "user@example.com";
ALTER USER user_name RENAME TO "user@example.com";
```

<!-- Auto Generated Markdown for FIR-38781 - Owned by jingtao.huang -->
**Resolved memory overuse during CSV import with large rows**    
Resolved a memory overconsumption problem that occurred when importing CSV files into existing tables.

<!-- Auto Generated Markdown for FIR-42413 - Owned by Jonathan Doron -->
**Resolved `EXPLAIN VACUUM` and `EXPLAIN` to improve error handling and result accuracy**    
The following behavior of `EXPLAIN VACUUM` has been updated:

1. If a table is fully vacuumed, no further actions are performed, and the message "Table is fully vacuumed, no vacuum jobs were executed" is returned to the user.
2. The `EXPLAIN VACUUM` output no longer returns an empty result when the vacuumed object is an Aggregating index.
3. `EXPLAIN` has been updated to show an error if the specified relation does not exist.
