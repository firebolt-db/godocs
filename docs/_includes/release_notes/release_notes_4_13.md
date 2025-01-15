# Firebolt Release Notes - Version 4.13

### Behavior Changes

<!-- FIR-37266 - Owned by Mariia Kaplun -->
**Removed secured objects from `information_schema` views**

Users can now only access information about objects for which they have the appropriate permissions or ownership in [information_schema views]({% link sql_reference/information-schema/views.md %}).

### New Features

<!-- Auto Generated Markdown for FIR-42091 - Owned by Tal Zelig -->
**Supported `GRANT ALL ON ACCOUNT` and `REVOKE ALL ON ACCOUNT` statements for role-based account privileges management**
The statements `GRANT ALL ON ACCOUNT account_name TO role_name` and `REVOKE ALL ON ACCOUNT account_name FROM role_name` are now supported. They grant or revoke all account-related privileges to the specified role `role_name`.


<!-- Auto Generated Markdown for FIR-42324 - Owned by David Boublil -->
**Supported arrays of arrays at any nested level in Parquet files**
Added support for arrays of arrays at any nested level in Parquet files.


### Performance Improvements

### Bug Fixes

<!-- Auto Generated Markdown for FIR-42575 - Owned by Tal Zelig -->
**Allowed the character `@` in usernames again**
We allow the character `@` in usernames again, which was previously restricted. The statements

```
CREATE USER "ex@mple";
ALTER USER user_name RENAME TO "ex@mple";
```

are now valid and do not cause errors.


<!-- Auto Generated Markdown for FIR-38781 - Owned by jingtao.huang -->
**Fixed memory overconsumption issue during CSV import with large rows into existing tables**
Resolved a memory overconsumption problem that occurred when importing CSV files with large rows into existing tables.


<!-- Auto Generated Markdown for FIR-42413 - Owned by Jonathan Doron -->
**Fixed `explain vacuum` and `explain` to improve error handling and result accuracy**
Fixed `explain vacuum` to:

1. Provide a correct error message when a table is already vacuumed.
2. Return non-empty results when running `explain vacuum` on an AI.

Also, fixed `explain` to display an error when the specified relation does not exist.
