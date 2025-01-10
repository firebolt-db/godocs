**Example**

The following code returns the cosine similarity between two vectors that point in very similar directions:

``` sql
SELECT VECTOR_COSINE_SIMILARITY([1, 2], [3, 4]) AS similarity;
```

**Returns**

| similarity (DOUBLE PRECISION) |
| :--- |
| 0.9838699100999074 |

**Example**

The following code returns the cosine similarity between two vectors that point in very different directions:

``` sql
SELECT VECTOR_COSINE_SIMILARITY([1, 2], [-3, -4]) AS similarity;
```

**Returns**

| similarity (DOUBLE PRECISION) |
| :--- |
| -0.9838699100999074 |

**Example**

The following code returns the cosine similarity between two vectors that are orthogonal to each other:

``` sql
SELECT VECTOR_COSINE_SIMILARITY([2, 0], [0, 2]) AS similarity;
```

**Returns**

| similarity (DOUBLE PRECISION) |
| :--- |
| 0 |