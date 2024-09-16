The following example calculates the maximum number in the array:
``` sql
SELECT ARRAY_MAX([1, 2, 3, 4]) AS res;
```

| res (INTEGER) |
| :--- |
| 4 |

This also works when the array contains `NULLs`:
``` sql
SELECT ARRAY_MAX([1, NULL, 2, NULL, 3, NULL, 4, NULL]) AS res;
```

| res (INTEGER) |
| :--- |
| 4 |

For empty arrays and arrays that only contain `NULL`, the `ARRAY_MAX` function will return `NULL`:
``` sql
SELECT ARRAY_MAX([]) as res1, ARRAY_MAX([NULL]) AS res2;
```

| res1 (TEXT) | res2 (TEXT) |
| :--- | :--- |
| NULL,NULL |