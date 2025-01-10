## Firebolt Release Notes - Version 4.9

### New Features

<!-- Auto Generated Markdown for FIR-37875 - Owned by Benjamin Wagner --> 
**Added the `enable_result_cache` setting for controlling query result caching during benchmarking**

You can set `enable_result_cache` to `FALSE` to disable the use of Firebolt's result cache, which is set to `TRUE` by default. Disabling result cashing can be useful for benchmarking query performance. When `enable_result_cache` is disabled, resubmitting the same query will recompute the results rather than retrieving them from cache. For more information, see [Result Cache]({% link Reference/system-settings.md %}#result-cache).

**Added `LAG` and `LEAD` support for negative offsets.**

The second parameter in both [LAG]({% link sql_reference/functions-reference/window/lag.md %}) and [LEAD]({% link sql_reference/functions-reference/window/lead.md %}) can now accept negative numbers. Given a negative number, a `LAG` will become a `LEAD` and vice versa. For example, `LAG(x,-5,3)` is the same as `LEAD(x,5,3)`.

### Performance Improvements

<!-- FIR-37296 - Owned by Timo Kersten -->
**Faster string searches for case-insensitive simple regular expressions in `REGEXP_LIKE`**

Simple regular expressions in [REGEXP_LIKE]({% link sql_reference/functions-reference/string/regexp-like.md %}) with case-insensitive matching, using the `i` flag, now use the same optimized string search implementation as [ILIKE]({% link sql_reference/functions-reference/string/ilike.md %}), achieving up to three times faster runtimes in observed cases.


### Bug Fixes

<!-- FIR-37296 - Owned by Pascal Schulze -->
**Empty character classes in regular expressions**

Fixed a rare case where empty character classes were mistakenly interpreted as valid character classes instead of being treated as raw characters. In cases like `[]a]`, the expression is now correctly interpreted as a pattern that matches any single character from the list `]a`, rather than treating `[]` as an empty character class followed by `a]`. 

<!-- FIR-37296 - Owned by Pascal Schulze -->
**Trailing backslash in regular expressions**

Fixed a rare case where invalid regular expressions with a trailing backslash `\` were accepted.
