---
layout: default
title: Functions glossary
description: Reference for SQL functions available in Firebolt.
grand_parent: SQL reference
parent: SQL functions
---

# Functions glossary

All Firebolt functions in alphabetical order.

| Name         | Function                                | Type    |
|:----------- |:------------------------------------------------ |:-------|
| [ABS](./numeric/abs.md) | Calculates the absolute value of an input value. | Numeric |
| [ACOS](./numeric/acos.md) | Calculates the arc cosine of a value. Returns NULL if the input value is higher than 1. | Numeric |
| [ALL_MATCH](./Lambda/all-match.md) | Returns 1 (true) when the condition evaluated on all elements of an array evaluate to true. Returns 0 (false) when any one comparison evaluates to false. | Lambda |
| [ANY_MATCH](./Lambda/any-match.md) | Returns 1 if at least one of the elements of an array matches the results of the function provided. Otherwise returns 0. | Lambda |
| [ANY_VALUE (ANY)](./aggregation/any_value.md) | Returns a single arbitrary value from the specified column. | Aggregation |
| [APPROX_COUNT_DISTINCT](./aggregation/approx-count-distinct.md) | Counts the approximate number of unique or not NULL values. | Aggregation |
| [APPROX_PERCENTILE](./aggregation/approx-percentile.md) | Returns an approximate value for the specified percentile based on the range of numbers returned by the input expression. | Aggregation |
| [ARRAY_AGG](./aggregate-array/array-agg.md) | Concatenates input values into an array. | Aggregate array |
| [ARRAY_CONCAT](./array/array-concat.md) | Combines one or more arrays that are passed as arguments. | Array |
| [ARRAY_COUNT](./Lambda/array-count.md) | Counts the number of elements in a boolean array for which `function(array[i])` evaluates to true, if a function is provided. If not provided, counts the number of elements in the array that evaluate to true. | Lambda |
| [ARRAY_COUNT_GLOBAL](./aggregate-array/array-count-global.md) | Returns the number of elements in the array column accumulated over all rows. | Aggregate array |
| [ARRAY_CUMULATIVE_SUM](./Lambda/array-cumulative-sum.md) | Returns an array of partial sums of elements from the source array (a cumulative sum). If a function input is provided, the values of the array elements are converted by this function before summing. | Lambda |
| [ARRAY_DISTINCT](./array/array-distinct.md) | Returns an array containing only the _unique_ elements of the given array. | Array |
| [ARRAY_FILL](./Lambda/array-fill.md) | Scans through the given array from the first to the last element and replaces `array[i]` with `array[i - 1]` if the input function returns 0. | Lambda |
| [ARRAY_FIRST](./Lambda/array-first.md) | Returns the first element in the given array for which the given function returns something other than 0. | Lambda |
| [ARRAY_FIRST_INDEX](./Lambda/array-first-index.md) | Returns the index of the first element in the indicated array for which the given function returns something other than 0. Index counting starts at 1. | Lambda |
| [ARRAY_INTERSECT](./array/array-intersect.md) | Evaluates all arrays that are provided as arguments and returns an array of any elements that are present in all the arrays. | Array |
| [ARRAY_JOIN (ARRAY_TO_STRING)](./array/array-join.md) | Concatenates an array of string elements using an optional delimiter. | Array |
| [ARRAY_MAX](./array/array-max.md) | Returns the maximum element in an array. | Array |
| [ARRAY_MAX_GLOBAL](./aggregate-array/array-max-global.md) | Returns the maximum element from all the array elements in each group. | Aggregate array |
| [ARRAY_MIN](./array/array-min.md) | Returns the minimum element in an array. | Array |
| [ARRAY_MIN_GLOBAL](./aggregate-array/array-min-global.md) | Returns the minimum element taken from all the array elements in each group. | Aggregate array |
| [ARRAY_REPLACE_BACKWARDS](./Lambda/array-replace-backwards.md) | Scans an array from the last to the first element and replaces each of the elements in that array with `array[i + 1]` if the specified function returns 0. The last element of the array is not replaced. | Lambda |
| [ARRAY_REVERSE](./array/array-reverse.md) | Returns an array of the same size and type as the original array, with the elements in reverse order. | Array |
| [ARRAY_SLICE](./array/array-slice.md) | Returns a slice of the array based on the indicated offset and length. | Array |
| [ARRAY_SORT](./Lambda/array-sort.md) | Returns the elements of the input array in ascending order. If the argument function is provided, the sorting order is determined by the result of applying the function on each element of the array. | Lambda |
| [ARRAY_SUM](./Lambda/array-sum.md) | Returns the sum of elements of the input array. If the argument function is provided, the values of the array elements are converted by this function before summing. | Lambda |
| [ARRAY_SUM_GLOBAL](./aggregate-array/array-sum-global.md) | Returns the sum of elements in the array column accumulated over the rows in each group. | Aggregate array |
| [ARRAY_TO_STRING](./array/array-to-string.md) | Concatenates an array of string elements using an optional delimiter. | Array |
| [ARRAY_UNIQ](./array/array-uniq.md) | Returns the number of different elements in the array if one argument is passed. If multiple arguments are passed, returns the number of different tuples of elements at corresponding positions in multiple arrays. | Array |
| [ASIN](./numeric/asin.md) | Calculates the arcsine of a value. Returns NULL if the input value is higher than 1. | Numeric |
| [ATAN](./numeric/atan2.md) | Calculates the arc tangent of the real number returned by the specified expression. | Numeric |
| [ATAN2](./numeric/atan.md) | Two-argument arc tangent function. Calculates the angle, in radians, between the specified positive x-axis value and the ray from the origin to the point `(y,x)`. | Numeric |
| [AVG](./aggregation/avg.md) | Calculates the average of an expression. | Aggregation |
| [AVG OVER](./window/avg-window.md) | Returns the average value within the requested window. | Window |
| [BTRIM](./string/btrim.md) | Removes all occurrences of optionally specified characters from both sides of a source string. If no trim parameter is specified, all occurrences of common whitespace (ASCII Decimal 32) characters from both sides of the specified source string are removed. | String |
| [CASE](./conditional-and-miscellaneous/case.md) | Conditional expression similar to if-then-else statements. | Conditional & miscellaneous |
| [CAST](./conditional-and-miscellaneous/cast.md) | Converts data types into other data types based on specified parameters. | Conditional & miscellaneous |
| [CBRT](./numeric/cbrt.md) | Returns the cubic-root of a non-negative numeric expression. | Numeric |
| [CEIL (CEILING)](./numeric/ceil.md) | Returns the smallest value that is greater than or equal to the input value. | Numeric |
| [CHECKSUM](./aggregation/checksum.md) | Calculates a hash value known as a checksum operation on a list of arguments. | Aggregation |
| [COALESCE](./conditional-and-miscellaneous/coalesce.md) | Checks from left to right for the first non-NULL argument found for each entry parameter pair. | Conditional & miscellaneous |
| [CONCAT (||)](./string/concat.md) | Concatenates the strings listed in the input without a separator. | String |
| [CONTAINS](./array/contains.md) | Returns 1 if a specified argument is present in the array, or 0 otherwise. | Array |
| [COS](./numeric/cos.md) | Trigonometric function that calculates the cosine of a specific value. | Numeric |
| [COT](./numeric/cot.md) | Calculates the cotangent. | Numeric |
| [COUNT](./aggregation/count.md) | Counts the number of rows or not NULL values. | Aggregation |
| [COUNT OVER](./window/count-window.md) | Count the number of values within the requested window. | Window |
| [CUME DIST](./window/cume-dist.md) | Calculates the relative rank (cumulative distribution) of the current row in relation to other rows in the same partition within an ordered data set, as `( rank + number_of_peers - 1 ) / ( total_rows )` where rank is the current row's rank within the partition, number_of_peers is the number of row values equal to the current row value (including the current row), and total_rows is the total number of rows in the partition. The return value ranges from 1/(total_rows) to 1. | Window |
| [CURRENT_DATE](./date-and-time/current-date.md) | Returns the current (local) date in the time zone specified in the session's `time_zone` setting. | Date & time |
| [CURRENT_TIMESTAMP](./date-and-time/current-timestamp.md) | Returns the current (local) timestamp in the time zone specified in the session's `time_zone` setting. | Date & time |
| [DATE_ADD](./date-and-time/date-add.md) | Calculates a new date or timestamp by adding or subtracting a specified number of time units from an indicated expression. | Date & time |
| [DATE_DIFF](./date-and-time/date-diff.md) | Calculates the difference between the start and end date by the indicated unit. | Date & time |
| [DATE_TRUNC](./date-and-time/date-trunc-new.md) | Truncates a date or timestamp value to the selected precision. | Date & time |
| [DECODE](./bytea/decode.md) | Decode binary data from a string. | Binary |
| [DEGREES](./numeric/degrees.md) | Converts a value in radians to degrees. | Numeric |
| [DENSE_RANK](./window/dense-rank.md) | Rank the current row within the requested window. | Window |
| [ELEMENT_AT](./array/element-at.md) | Returns the element at a location index from the given array. Indexes in an array begin at position 1. | Array |
| [ENCODE](./bytea/encode.md) | Encode binary data into a string. | Binary |
| [EXP](./numeric/exp.md) | Returns the `REAL` value of the constant _e_ raised to the power of a specified number. | Numeric |
| [EXTRACT](./date-and-time/extract-new.md) | Retrieves the time unit from a date or timestamp value. | Date & time |
| [EXTRACT_ALL](./string/extract-all.md) | Extracts fragments within a string that match a specified regex pattern. String fragments that match are returned as an array of strings. | String |
| [FILTER](./Lambda/filter.md) | Returns an array containing the elements from the input array for which the given Lambda function returns something other than 0. The function can receive one or more arrays as its arguments. When multiple arrays are provided to the function, the function will evaluate the current elements from each array as its parameter. | Lambda |
| [FIRST_VALUE](./window/first-value.md) | Returns the first value evaluated in the specified window frame. If there are no rows in the window frame, returns NULL. | Window |
| [FLATTEN](./array/flatten.md) | Converts an array of arrays into a flat array. For every element that is an array, this function extracts its elements into the new array. | Array |
| [FLOOR](./numeric/floor.md) | Returns the largest round number that is less than or equal to the input value. | Numeric |
| [GEN_RANDOM_UUID](./string/gen-random-uuid.md) | Returns a version 4 universally unique identifier (UUID) according to RFC-4122. | String |
| [GENERATE_SERIES](./conditional-and-miscellaneous/generate-series.md) | Generates a single rowset of values from `start` to `stop`, with a step size of `step` - a table-valued function. | Conditional & miscellaneous |
| [HLL_COUNT_DISTINCT](./aggregation/hll-count-distinct.md) | Counts the approximate number of unique or not NULL values, to the precision specified. | Aggregation |
| [IFNULL](./conditional-and-miscellaneous/ifnull.md) | Compares two expressions. Returns the first input expression if it’s non-NULL, otherwise returns the second. | Conditional & miscellaneous |
| [ILIKE](./string/ilike.md) | Allows matching of strings based on comparison to a pattern, case-insensitively. | String |
| [INDEX_OF](./array/index-of.md) | Returns the index position of the first occurrence of the element in the array (or 0 if not found). | Array |
| [JSON_EXTRACT](./JSON/json-extract.md) | Takes an expression containing a JSON document, a JSON pointer expression, and an expected data type parameter. If the key specified using the JSON pointer expression exists, and its type conforms with the expected data type parameter, returns the value of the data type specified. Otherwise, returns NULL. | Semi-structured data |
| [JSON_EXTRACT_ARRAY_RAW](./JSON/json-extract-array-raw.md) | Returns a string representation of a JSON array pointed by the supplied JSON pointer. | Semi-structured data |
| [JSON_EXTRACT_KEYS](./JSON/json-extract-keys.md) | Returns an array of strings containing the keys at the nesting level indicated by the specified JSON pointer. | Semi-structured data |
| [JSON_EXTRACT_RAW](./JSON/json-extract-raw.md) | Returns a string representation of the scalar or sub-object under the key indicated by the specified JSON pointer if the key exists. | Semi-structured data |
| [JSON_EXTRACT_VALUES](./JSON/json-extract-values.md) | Returns an array of string values from a JSON document using the key location specified by the specifed JSON pointer. | Semi-structured data |
| [LAG](./window/lag.md) | Returns the value of the input expression at the given offset before the current row within the requested window. | Window |
| [LEAD](./window/lead.md) | Returns values from the row after the current row within the requested window. | Window |
| [LENGTH](./string/like.md) | Calculates the length of the input string. | String |
| [LENGTH (array)](./array/length.md) | Returns the length of (number of elements in) the given array. | Array |
| [LIKE](./string/like.md) | Allows matching of strings based on comparison to a pattern, case-sensitively. | String |
| [LOCALTIMESTAMP](./date-and-time/localtimestamp.md) | Returns the current local timestamp in the time zone specified in the session's `time_zone` setting. | Date & time |
| [LOG](./numeric/log.md) | Returns the common (base 10) logarithm of a numerical expression, or the logarithm to an arbitrary base if specified as the first argument. | Numeric |
| [LOWER](./string/lower.md) | Converts the input string to lowercase characters. | String |
| [LPAD](./string/lpad.md) | Adds a specified pad string to the start of the string repetitively up until the length of the resulting string is equivalent to an indicated length. | String |
| [LTRIM](./string/ltrim.md) | Removes all occurrences of optionally specified characters from the left side of a source string. If no trim parameter is specified, all occurrences of common whitespace (ASCII Decimal 32) characters from the left side of the specified source string are removed. | String |
| [MATCH](./string/match.md) | Checks whether the input expression matches the specified regular expression pattern, which is a RE2 regular expression.  Returns 0 if it doesn’t match, or 1 if it matches. | String |
| [MATCH_ANY](./string/match-any.md) | The same as `MATCH`, but searches for a match with one or more more regular expression patterns. Returns 0 if none of the regular expressions match and 1 if any of the patterns match. | String |
| [MAX](./aggregation/max.md) | Calculates the maximum value of an expression across all input values. | Aggregation | 
| [MAX OVER](./window/max-window.md) | Returns the maximum value within the requested window. | Window | 
| [MAX_BY](./aggregation/max-by.md) | Returns the value of the specified input column at the row with the maximum value in the specified value column. | Aggregation 
| [MEDIAN](./aggregation/median.md) | Calculates an approximate median for a given column. | Aggregation | 
| [MIN](./aggregation/min.md) | Calculates the minimum value of an expression across all input values. | Aggregation |
| [MIN OVER](./window/min-window.md) | Returns the maximum value within the requested window. | Window | 
| [MIN_BY](./aggregation/min-by.md) | Returns the value of the specified input column at the row with the minimum value in the specified value column. | Aggregation | 
| [MOD](./numeric/mod.md) | Calculates the remainder after dividing two values. | Numeric |
| [NTH_VALUE](./window/nth-value.md) | Returns the value evaluated of the nth row of the specified window frame (starting at the first row). If the specified row does not exist, NTH_VALUE returns NULL. | Window | 
| [NTILE](./window/ntile.md) | Divides an ordered data set equally into the number of buckets specified by the argument value. Buckets are sequentially numbered 1 through the argument value. | Window | 
| [NULLIF](./conditional-and-miscellaneous/nullif.md) | Compares two expressions. Returns NULL if the expressions are equal. Returns the result of the first if they are not equal. | Conditional & miscellaneous |
| [PERCENT_RANK](./window/percent-rank.md) | Calculates the relative rank of the current row within an ordered data set, as `( rank - 1 ) / ( rows - 1 )` where rank is the current row's rank within the partition, and rows is the number of rows in the partition. PERCENT_RANK always returns values from 0 to 1 inclusive. The first row in any set has a PERCENT_RANK of 0. | Window | 
| [PERCENTILE_CONT](./aggregation/percentile-cont.md) | Calculates a percentile, assuming a continuous distribution of values of the input expression defined. Results are interpolated, rather than matching any of the specific column values. | Aggregation |
| [PERCENTILE_CONT OVER](./window/percentile-cont-window.md) | Calculates a percentile over a partition, assuming a continuous distribution of values defined. Results are interpolated, rather than matching any of the specific column values. | Window |
| [PERCENTILE_DISC](./aggregation/percentile-disc.md) | Returns a percentile for an ordered data set. The result is equal to a specific column value, the smallest distributed value that is greater than or equal to the percentile value specified.  | Aggregation |
| [PERCENTILE_DISC OVER](./window/percentile-disc-window.md) | Returns a percentile over a partition for an ordered data set. The result is equal to a specific column value, the smallest distributed value that is greater than or equal to the percentile specified. | Window |
| [PI](./numeric/pi.md) | Calculates π as a `REAL` value. | Numeric |
| [POW (POWER)](./numeric/pow.md) | Returns a number raised to the specified power. | Numeric |
| [RADIANS](./numeric/radians.md) | Converts degrees to radians as a `REAL` value. | Numeric |
| [RANDOM](./numeric/random.md) | Returns a pseudo-random unsigned value greater than 0 and less than 1 of type `DOUBLE PRECISION`. | Numeric |
| [RANK](./window/rank.md) | Rank the current row within the requested window with gaps. | Window |
| [REDUCE](./array/reduce.md) | Applies an aggregate function on the elements of the array and returns its result. | Array |
| [REGEXP_EXTRACT](./string/regexp-extract.md) | Returns the first match of a pattern within the input expression. If the pattern does not match, returns NULL. | String |
| [REGEXP_EXTRACT_ALL](./string/regexp-extract-all.md) | Returns an array that contains all matches of a pattern within the given input expression. If the pattern does not match, returns an empty array. | String |
| [REGEXP_LIKE](./string/regexp-like.md) | Checks whether a text pattern matches a regular expression string. Returns 0 if it doesn’t match, or 1 if it matches. | String |
| [REGEXP_MATCHES](./string/regexp-matches.md) | Returns an array that contains either the match or all defined subgroups of the first match of the regular expression pattern. Returns an empty array if the pattern does not match. | String |
| [REGEXP_REPLACE](./string/regexp-replace.md) | Matches a pattern in the input string and replaces the first matched portion (from the left) with the specified replacement. | String |
| [REPEAT](./string/repeat.md) | Repeats the provided string a requested number of times. | String |
| [REPLACE](./string/replace.md) | Replaces all occurrences of the given pattern substring within the input expression with a replacement substring. | String |
| [REVERSE](./string/reverse.md) | Returns a string of the same size as the original string, with the elements in reverse order. | String |
| [ROUND](./numeric/round.md) | Rounds a value to a specified number of decimal places. | Numeric |
| [ROW_NUMBER](./window/row-number.md) | Returns a unique row number for each row within the requested window. | Window |
| [RPAD](./string/rpad.md) | Adds a specified pad string to the end of the string repetitively up until the length of the resulting string is equivalent to an indicated length. | String |
| [RTRIM](./string/rtrim.md) | Removes all occurrences of optionally specified characters from the right side of a source string. If no trim parameter is specified, all occurrences of common whitespace (ASCII Decimal 32) characters from the right side of the specified source string are removed. | String |
| [SIGN](./numeric/sign.md) | Returns the sign of a number according to the table below. | Numeric |
| [SIN](./numeric/sin.md) | Trigonometric function that calculates the sine of a provided value. | Numeric |
| [SPLIT](./string/split.md) | This function splits a given string by a given separator and returns the result in an array of strings. | String |
| [SPLIT_PART](./string/split-part.md) | Divides a string based on a specified delimiter into an array of substrings. The string in the specified index is returned, with 1 being the first index. If the string separator is empty, the string is divided into an array of single characters. | String |
| [SQRT](./numeric/sqrt.md) | Returns the square root of a non-negative numeric expression. | Numeric |
| [STDDEV_SAMP](./aggregation/stddev-samp.md) | Computes the standard deviation of a sample consisting of a numeric expression. | Aggregation |
| [STRPOS](./string/strpos.md) | Returns the position (in bytes) of the substring found in the string, starting from 1. The returned value is for the first matching value, and not for any subsequent valid matches. In case the substring does not exist, functions will return 0. | String |
| [SUBSTRING](./string/substring.md) | Returns a substring starting at the character indicated by the start index and including the number of characters defined. Character indexing starts at index 1. | String |
| [SUM](./aggregation/sum.md) | Calculates the sum of an expression. | Aggregation |
| [SUM OVER](./window/sum-window.md) | Calculate the sum of the values within the requested window. | Window |
| [TAN](./numeric/tan.md) | Calculates the tangent. | Numeric |
| [TO_CHAR](./date-and-time/to-char-new.md) | Converts a date or timestamp value to a formatted string. | Date & time |
| [TO_TIMESTAMP](./string/to-timestamp.md) | Converts a string to timestamp with time zone. | Date & time |
| [TRANSFORM](./Lambda/transform.md) | Returns an array by applying the specified on each element of the input array. | Lambda |
| [TRIM](./string/trim.md) | Removes all specified characters from the start, end, or both sides of a string. By default removes all consecutive occurrences of common whitespace (ASCII character 32) from both ends of a string. | String |
| [TRUNC](./numeric/trunc.md) | Returns the rounded absolute value of a numeric value. The returned value will always be rounded to less than the original value. | Numeric |
| [TRY_CAST](./conditional-and-miscellaneous/try-cast.md) | Converts data types into other data types based on the specified parameters. If the conversion cannot be performed, returns a NULL. | Conditional & miscellaneous |
| [UPPER](./string/upper.md) | Converts the input string to uppercase characters. | String |
| [URL_DECODE](./string/url_decode.md) | Decodes percent-encoded characters and replaces them with their binary value. | String |
| [URL_ENCODE](./string/url_encode.md) | Encodes all characters that are not unreserved using percent-encoding. | String |
| [VERSION](./conditional-and-miscellaneous/version.md) | Returns the version number information for the Firebolt engine. | Conditional & miscellaneous |