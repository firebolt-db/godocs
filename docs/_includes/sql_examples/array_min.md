**Example**
{% raw %}
The following example calculates the minimum number in the specified array:

``` sql
SELECT ARRAY_MIN([1, 2, 3, 4]) AS res;
```
**Returns**

| res (INTEGER) |
| :--- |
| 1 |
{% endraw %}

**Example**
{% raw %}
`ARRAY_MIN` returns the minimum element, ignoring `NULL` values in the array:

``` sql
SELECT ARRAY_MIN([1, NULL, 2, NULL, 3, NULL, 4, NULL]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 1 |
{% endraw %}

**Example**
{% raw %}
For empty arrays and arrays that only contain `NULL`, the `ARRAY_MIN` function will return `NULL`:

``` sql
SELECT ARRAY_MIN([]) as res1, ARRAY_MIN([NULL]) AS res2;
```

**Returns**

| res1 (TEXT) | res2 (TEXT) |
| :--- | :--- |
| NULL | NULL |
{% endraw %}
