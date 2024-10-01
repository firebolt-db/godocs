**Example**
The following code example checks if an array contains the value `esimpson` as the result `is_he_playing`:

``` sql
SELECT ARRAY_ANY_MATCH(x -> x = 'esimpson', [ 'kennethpark', 'sabrina21', 'steven70']) AS is_he_playing;
```

**Returns**
The previous code returns `FALSE` because the array does not contain the specified value:

| is_he_playing (BOOLEAN) |
| :--- |
| f |

**Example**
The following code example checks if each element in the first array is divisible by the corresponding element in the second array in a result labeled `divisible`:

``` sql
SELECT ARRAY_ANY_MATCH(x, y -> (x % y) = 0, [ 10, 20, 30, 45 ], [ 12, 3, 42, 15]) AS divisible;
```

**Returns**
The previous code returns `TRUE` because each element in the first array is divisible by its corresponding element in the second array:

| divisible (BOOLEAN) |
| :--- |
| t |

**Example**
The following code example evaluates multiple arrays using `ARRAY_ANY_MATCH`:

``` sql
SELECT ARRAY_ANY_MATCH([])          as empty,
ARRAY_ANY_MATCH([true])         as single_true,
ARRAY_ANY_MATCH([false])        as single_false,
ARRAY_ANY_MATCH([NULL])         as single_null ,
ARRAY_ANY_MATCH([false, NULL])  as false_and_null;
```

**Returns**
The previous code returns `FALSE` for the empty array, `TRUE` for the `[TRUE]` array, `FALSE` for the `[FALSE]` array, `NULL` for the `[NULL]` array, and `FALSE` for the `[FALSE, NULL]` array:

| empty (BOOLEAN) | single_true (BOOLEAN) | single_false (BOOLEAN) | single_null (BOOLEAN) | false_and_null (BOOLEAN) |
| :--- | :--- | :--- | :--- | :--- |
| f | t | f | NULL | NULL |
