

The following example returns the Manhattan distance between two vectors:
``` sql
SELECT VECTOR_MANHATTAN_DISTANCE([1, 4], [3, 2]) AS distance;
```
In the previous example, the Manhattan distance is calculated as the sum of absolute differences: |3 - 1| + |2 - 4| = 4.

| distance (DOUBLE) |
| :--- |
| 4 |

