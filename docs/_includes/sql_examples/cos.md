The following query calculates the cosine of 0:
``` sql
SELECT COS(0) as result;
```

| result (DOUBLE PRECISION) |
| :--- |
| 1 |

The following query calculates the cosine of pi:
``` sql
SELECT ROUND(COS(PI()), 5) as result;
```

| result (DOUBLE PRECISION) |
| :--- |
| -1 |