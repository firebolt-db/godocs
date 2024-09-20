The following example returns the squared Euclidean distance between two vectors:
``` sql
SELECT VECTOR_SQUARED_EUCLIDEAN_DISTANCE([1, 2], [3, 4]) AS distance;
```

| distance (DOUBLE) |
| :--- |
| 8 |

The following example returns the squared Euclidean distance between two identical vectors:
``` sql
SELECT VECTOR_SQUARED_EUCLIDEAN_DISTANCE([1, 1], [1, 1]) AS distance;
```

| distance (DOUBLE) |
| :--- |
| 0 |

The following example returns the squared Euclidean distance between two vectors that are very far apart:
``` sql
SELECT VECTOR_SQUARED_EUCLIDEAN_DISTANCE([1, 1], [10, 10]) AS distance;
```

| distance (DOUBLE) |
| :--- |
| 162 |