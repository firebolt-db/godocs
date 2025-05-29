``` sql
CREATE TABLE data_to_count AS
SELECT *
FROM generate_series(0, 10000000, 3) a;
```

``` sql
CREATE TABLE data_to_count2 AS
SELECT *
FROM generate_series(0, 10000000, 2) a;
```

``` sql
CREATE TABLE sketch_of_data_to_count AS
SELECT hll_count_build(a) a
FROM data_to_count;
```

``` sql
INSERT INTO sketch_of_data_to_count
SELECT hll_count_build(a)
FROM data_to_count2;
```

``` sql
SELECT hll_count_estimate(a) AS hll_estimate
FROM sketch_of_data_to_count
ORDER BY 1;
```

| hll_estimate (BIGINT) |
| :--- |
| 3291008 |
| 4948957 |

``` sql
SELECT hll_count_estimate(hll_count_merge(a)) AS hll_estimate
FROM sketch_of_data_to_count;
```

| hll_estimate (BIGINT) |
| :--- |
| 6606880 |