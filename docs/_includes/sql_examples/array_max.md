**Example**
{% raw %}
The following example calculates the maximum number in the specified array:

``` sql
SELECT ARRAY_MAX([1, 2, 3, 4]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 4 |
{% endraw %}

**Example**
{% raw %}
`ARRAY_MAX` returns the maximum element, ignoring `NULL` values in the array:

``` sql
SELECT ARRAY_MAX([1, NULL, 2, NULL, 3, NULL, 4, NULL]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 4 |
{% endraw %}

**Example**
{% raw %}
For empty arrays and arrays that only contain `NULL`, the `ARRAY_MAX` function will return `NULL`:

``` sql
SELECT ARRAY_MAX([]) as res1, ARRAY_MAX([NULL]) AS res2;
```

**Returns**

| res1 (TEXT) | res2 (TEXT) |
| :--- | :--- |
| NULL | NULL |
{% endraw %}
