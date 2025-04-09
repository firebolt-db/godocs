**Example**
{% raw %}
``` sql
CREATE TABLE data_to_count AS
SELECT *
FROM generate_series(0, 10000000, 3) a;
```
{% endraw %}

{% raw %}
``` sql
CREATE TABLE data_to_count2 AS
SELECT *
FROM generate_series(0, 10000000, 2) a;
```
{% endraw %}

{% raw %}
``` sql
CREATE TABLE sketch_of_data_to_count AS
SELECT hll_count_build(a) a
FROM data_to_count;
```
{% endraw %}

{% raw %}
``` sql
INSERT INTO sketch_of_data_to_count
SELECT hll_count_build(a)
FROM data_to_count2;
```
{% endraw %}

{% raw %}
``` sql
SELECT hll_count_estimate(a) AS hll_estimate
FROM sketch_of_data_to_count
ORDER BY 1;
```

**Returns**

| hll_estimate (BIGINT) |
| :--- |
| 3,291,008 |
| 4,948,957 |
{% endraw %}

**Query**
{% raw %}
``` sql
SELECT hll_count_estimate(hll_count_merge(a)) AS hll_estimate
FROM sketch_of_data_to_count;
```
**Returns**

| hll_estimate (BIGINT) |
| :--- |
| 6,606,880 |
{% endraw %}