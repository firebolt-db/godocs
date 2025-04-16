In the following example, the only element shared between all three arrays is the `1`:
``` sql
SELECT ARRAY_INTERSECT([ 1, 2, 3 ], [ 0, 1 ], [ 1, 5 ]) as result;
```

| result (ARRAY(INTEGER)) |
| :--- |
| {1} |

Passing in one argument array is allowed:
``` sql
SELECT ARRAY_INTERSECT([ 'red', 'maroon', 'crimson' ]) as colors;
```

| colors (ARRAY(TEXT)) |
| :--- |
| {crimson,maroon,red} |

In the following example, `ARRAY_SORT` is used to ensure the results are in ascending order:
``` sql
SELECT ARRAY_SORT(
        ARRAY_INTERSECT([ 5, 4, 3, 2, 1 ],[ 5, 3, 1 ])
    ) as sorted;
```

| sorted (ARRAY(INTEGER)) |
| :--- |
| {1,3,5} |

`NULL` can appear in the intersection, only if it appears in all the argument arrays:
``` sql
SELECT ARRAY_INTERSECT([ 1, 9, NULL ],[ 8, 9, NULL ], [4, 9, NULL]) as contains_null;
```

| contains_null (ARRAY(INTEGER)) |
| :--- |
| {NULL,9} |

The result does not contain duplicates, even if the same value appears multiple times in all argument arrays:
``` sql
SELECT ARRAY_INTERSECT([ 1, 2, 2, 8 ],[ 1, 2, 2, 2, 6 ]) as unique;
```

| unique (ARRAY(INTEGER)) |
| :--- |
| {2,1} |

Arbitrarily nested arrays are also supported:
``` sql
SELECT ARRAY_INTERSECT([ [1], [2], NULL, [1,2] ], [ [1,2], NULL ]) as nested;
```

| nested (ARRAY(ARRAY(INTEGER))) |
| :--- |
| {NULL,{1,2}} |