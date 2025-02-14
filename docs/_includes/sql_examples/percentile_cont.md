The following query choose the 20% percentile value that exists in the input set
``` sql
SELECT PERCENTILE_CONT(0.2) WITHIN GROUP (ORDER BY x) as result FROM generate_series(0, 10) as x;
```

| result (DOUBLE PRECISION) |
| :--- |
| 2 |

The following query choose the 2 values near the 20% percentile value that exists in the input range which are 2, 3 and interpulate between them as described in the formula above
``` sql
SELECT PERCENTILE_CONT(0.2) WITHIN GROUP (ORDER BY x) as result FROM generate_series(0, 11) as x;
```

| result (DOUBLE PRECISION) |
| :--- |
| 2.2 |