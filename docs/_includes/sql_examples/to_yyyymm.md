``` sql
SELECT TO_YYYYMM('2025-04-03') as yyyymm, TO_YYYYMMDD('2025-04-03') as yyyymmdd;
```

| yyyymm (INTEGER) | yyyymmdd (INTEGER) |
| :--- | :--- |
| 202504 | 20250403 |

``` sql
SELECT TO_YYYYMM('1920-12-30') as yyyymm, TO_YYYYMMDD('1920-12-30') as yyyymmdd;
```

| yyyymm (INTEGER) | yyyymmdd (INTEGER) |
| :--- | :--- |
| 192012 | 19201230 |