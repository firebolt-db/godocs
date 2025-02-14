The following query calculates the tangent of 1.57 radians. 1.57 is approximately pi/2:
``` sql
SELECT TAN(1.57) as result;
```

| result (DOUBLE PRECISION) |
| :--- |
| 1255.7655915007897 |

The following query calculates the tangent of pi:
``` sql
SELECT ROUND(TAN(PI()), 5) as result;
```

| result (DOUBLE PRECISION) |
| :--- |
| -0 |