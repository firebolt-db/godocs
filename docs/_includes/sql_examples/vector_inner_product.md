The following example returns the inner product of two vectors that have similar directions and magnitudes:
``` sql
SELECT VECTOR_INNER_PRODUCT([1, 2], [3, 4]) AS product;
```

| product (DOUBLE) |
| :--- |
| 11 |

The following example returns the inner product of two vectors that are orthogonal to each other:
``` sql
SELECT VECTOR_INNER_PRODUCT([3, 4], [-4, 3]) AS product;
```

| product (DOUBLE) |
| :--- |
| 0 |

The following example returns the inner product of two vectors that are pointing in very different directions that are not orthogonal:
``` sql
SELECT VECTOR_INNER_PRODUCT([3, 4], [4, -2]) AS product;
```

| product (DOUBLE) |
| :--- |
| 4 |