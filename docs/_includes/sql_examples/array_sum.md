**Example**
{% raw %}
The following example calculates the sum of all numbers in the specified array:

``` sql
SELECT ARRAY_SUM([1, 2, 3, 4]) AS res;
```

**Returns**

| res (BIGINT) |
| :--- |
| 10 |
{% endraw %}

**Example**
{% raw %}
The following example shows that `ARRAY_SUM` ignores `NULL` values when calculating the sum:

``` sql
SELECT ARRAY_SUM([1, NULL, 2, NULL, 3, NULL, 4, NULL]) AS res;
```

**Returns**

| res (BIGINT) |
| :--- |
| 10 |
{% endraw %}

**Example**
{% raw %}
For empty arrays and arrays that contain only `NULL` values, `ARRAY_SUM` returns `NULL`, as shown in the following code example that uses explicit typecasting:

``` sql
SELECT ARRAY_SUM([]::ARRAY(INT)) as res1, ARRAY_SUM([NULL]::ARRAY(INT)) AS res2;
```

**Returns**

| res1 (BIGINT) | res2 (BIGINT) |
| :--- | :--- |
| NULL | NULL |
{% endraw %}
