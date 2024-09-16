{% raw %}
The following example calculates the sum of all numbers in the array:
``` sql
SELECT ARRAY_SUM([1, 2, 3, 4]) AS res;
```

| res (BIGINT) |
| :--- |
| 10 |
{% endraw %}

{% raw %}
`NULL` values are ignored in the sum:
``` sql
SELECT ARRAY_SUM([1, NULL, 2, NULL, 3, NULL, 4, NULL]) AS res;
```

| res (BIGINT) |
| :--- |
| 10 |
{% endraw %}

{% raw %}
For empty arrays and arrays that only contain `NULL`, the `ARRAY_SUM` function will return `NULL`:
``` sql
SELECT ARRAY_SUM([]::ARRAY(INT)) as res1, ARRAY_SUM([NULL]::ARRAY(INT)) AS res2;
```

| res1 (BIGINT) | res2 (BIGINT) |
| :--- | :--- |
| NULL | NULL |
{% endraw %}
