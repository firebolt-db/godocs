The following code example checks if all elements in the array end with `'2024'`:

``` sql
SELECT ARRAY_ALL_MATCH(name -> name like '%2024', [ 'kennethpark2024', 'sabrina2024', 'steven2024']) AS result;
```

**Returns**
The previous code returns `TRUE` because each name in the array matches the condition:

| result (BOOLEAN) |
| :--- |
| t |

**Example**

The following code example checks if each element in the first array is divisible by the corresponding element in the second array, and returns `TRUE` if all pairs satisfy the condition:

``` sql
SELECT ARRAY_ALL_MATCH(x, y -> (x % y) = 0, [ 10, 20, 30, 45 ], [ 5, 10, 2, 15]) AS divisible;
```

**Returns**
The previous code returns `TRUE` because all pairs in the first array are divisible by its corresponding second array:

| divisible (BOOLEAN) |
| :--- |
| t |

**Example**
The following code example evaluates multiple arrays using `ARRAY_ALL_MATCH`:

``` sql
SELECT ARRAY_ALL_MATCH([])              as empty,
       ARRAY_ALL_MATCH([true])          as single_true,
       ARRAY_ALL_MATCH([false])         as single_false,
       ARRAY_ALL_MATCH([NULL])          as single_null,
       ARRAY_ALL_MATCH([false, NULL])   as false_and_null;
```

**RETURNS**
The previous code returns `TRUE` for an empty array, `TRUE` for an array with `TRUE`, `FALSE` for any array with `FALSE`, `NULL` for an array with `NULL`, and `FALSE` for an array containing both `FALSE` and `NULL`:

| empty (BOOLEAN) | single_true (BOOLEAN) | single_false (BOOLEAN) | single_null (BOOLEAN) | false_and_null (BOOLEAN) |
| :--- | :--- | :--- | :--- | :--- |
| t | t | f | NULL | f |