# Firebolt Release Notes - Version 4.5

## New Features

<!-- Auto Generated Markdown for FIR-35466 - Owned by Mosha Pasumansky -->
### Allowed casting from `TEXT` to `DATE` with truncation of timestamp-related fields
Casting from `TEXT` to `DATE` now supports text values containing fields related to timestamps. These fields are accepted, but truncated during conversion to `DATE`. 

The following code example casts the `TEXT` representation of the timestamp `2024-08-07 12:34:56.789` to the `DATE` data type. The conversion truncates the time portion, leaving only the date, as follows:

Example:
```
SELECT '2024-08-07 12:34:56.789'::DATE`
```

Results in
```
DATE `2024-08-07`
```


<!-- Auto Generated Markdown for FIR-35408 - Owned by Kfir Yehuda -->
### Added the `CONVERT_FROM` function
Added the `CONVERT_FROM` function that converts a `BYTEA` value with a given encoding to a `TEXT` value encoded in UTF-8.

### Added the BITWISE aggregate functions
Added support for the following functions: BIT_OR (bitwise OR), BIT_XOR (bitwise exclusive OR), and BIT_AND (bitwise AND).

## Bug Fixes

<!-- Auto Generated Markdown for FIR-35688 - Owned by Asya Shneerson -->
### Updated `created` and `last_altered` column types in `information_schema.views` from `TIMESTAMP` to `TIMESTAMPTZ`
The data types of the `created` and `last_altered` columns in `information_schema.views` have been changed from `TIMESTAMP` to `TIMESTAMPTZ`.


<!-- Auto Generated Markdown for FIR-36063 - Owned by Timo Kersten -->
### Fixed runtime constant handling in the sort operator
Fixed the handling of runtime constants in the sort operator. 
Now, the sort operator can be correctly combined with `GENERATE_SERIES`.
For example, the query `SELECT x, GENERATE_SERIES(1,7,3) FROM GENERATE_SERIES(1,3) t(x)` now correctly displays values `1` to `3` in the first column, instead of just `1`.
