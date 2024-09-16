In the following example, `ARRAY_DISTINCT` removes all duplicate values from the array:
``` sql
SELECT ARRAY_DISTINCT([1, 2, 3, 1, 2, 3]) AS res;
```

| res (ARRAY(INTEGER)) |
| :--- |
| {1,2,3} |

If the input array has at least one `NULL`, the output contains exactly one `NULL`:
``` sql
SELECT ARRAY_DISTINCT([1, 2, 3, NULL, 1, 2, 3, NULL]) AS res;
```

| res (ARRAY(INTEGER)) |
| :--- |
| {1,2,3,NULL} |