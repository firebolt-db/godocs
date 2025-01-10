**Example**

The following code returns the Manhattan distance between two vectors:
The Manhattan distance is calculated as the sum of absolute differences: |3 - 1| + |2 - 4| = 4.

``` sql
SELECT VECTOR_MANHATTAN_DISTANCE([1, 4], [3, 2]) AS distance;
```

**Returns**

| distance (DOUBLE PRECISION) |
| :--- |
| 4 |