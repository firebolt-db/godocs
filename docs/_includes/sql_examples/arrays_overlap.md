The following example returns `TRUE` because all input arrays contain the element `2`.
``` sql
SELECT ARRAYS_OVERLAP(ARRAY[1, 2], ARRAY[2, 4], ARRAY[2, 6]) AS have_overlap
```

| have_overlap (BOOLEAN) |
| :--- |
| t |

The following example returns `FALSE` because no element appears in all input arrays.
``` sql
SELECT ARRAYS_OVERLAP(ARRAY[1, 2], ARRAY[2, 4], ARRAY[1, 6]) AS have_overlap
```

| have_overlap (BOOLEAN) |
| :--- |
| f |

The following example returns `FALSE` because no non-`NULL` element appears in all input arrays.
``` sql
SELECT ARRAYS_OVERLAP(ARRAY[NULL], ARRAY[NULL]) AS have_overlap
```

| have_overlap (BOOLEAN) |
| :--- |
| f |

The following example returns `NULL` because one of the inputs is `NULL`.
``` sql
SELECT ARRAYS_OVERLAP(NULL, ARRAY[1, 2]) AS have_overlap
```

| have_overlap (BOOLEAN) |
| :--- |
| NULL |