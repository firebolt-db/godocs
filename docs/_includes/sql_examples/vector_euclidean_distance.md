The following example returns the Euclidean distance between two vectors:
``` sql
SELECT VECTOR_EUCLIDEAN_DISTANCE([1, 2], [3, 4]) AS distance;
```

| distance (DOUBLE) |
| :--- |
| 2.8284271247461903 |