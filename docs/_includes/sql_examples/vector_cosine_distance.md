The following example returns the cosine distance between two vectors:
``` sql
SELECT VECTOR_COSINE_DISTANCE([1, 2], [3, 4]) AS distance;
```

| distance (DOUBLE) |
| :--- |
| 0.01613008990009257 |