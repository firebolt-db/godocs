The following array has three distinct values:
``` sql
SELECT ARRAY_COUNT_DISTINCT([1, 2, 3]) AS res;
```

| res (INTEGER) |
| :--- |
| 3 |

`NULLs` do not contribute to the distinct count:
``` sql
SELECT ARRAY_COUNT_DISTINCT([1, NULL, 2, NULL, 3]) AS res;
```

| res (INTEGER) |
| :--- |
| 3 |

Adding duplicate values does not either:
``` sql
SELECT ARRAY_COUNT_DISTINCT([1, NULL, 2, NULL, 3, 1, 2, 3]) AS res;
```

| res (INTEGER) |
| :--- |
| 3 |