Check if all player nicknames end with `'2024'`:
``` sql
SELECT ARRAY_ALL_MATCH(name -> name like '%2024', [ 'kennethpark2024', 'sabrina2024', 'steven2024']) AS result;
```

| result (BOOLEAN) |
| :--- |
| t |

Check if all elements in the first array can be divided by the elements in the second array:
``` sql
SELECT ARRAY_ALL_MATCH(x, y -> (x % y) = 0, [ 10, 20, 30, 45 ], [ 5, 10, 2, 15]) AS divisable;
```

| divisable (BOOLEAN) |
| :--- |
| t |

Check if all elements in an input array are `true`:
``` sql
SELECT ARRAY_ALL_MATCH([])          as empty,
    ARRAY_ALL_MATCH([true])         as single_true,
    ARRAY_ALL_MATCH([false])        as single_false,
    ARRAY_ALL_MATCH([NULL])         as single_null ,
    ARRAY_ALL_MATCH([false, NULL])  as false_and_null;
```

| empty (BOOLEAN) | single_true (BOOLEAN) | single_false (BOOLEAN) | single_null (BOOLEAN) | false_and_null (BOOLEAN) |
| :--- | :--- | :--- | :--- | :--- |
| t | t | f | NULL | f |