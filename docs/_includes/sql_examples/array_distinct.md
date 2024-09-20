**Example**
{% raw %}
In the following example, `ARRAY_DISTINCT` removes all duplicate values from the array:

``` sql
SELECT ARRAY_DISTINCT([1, 2, 3, 1, 2, 3]) AS res;
```

**Returns**

| res (ARRAY(INTEGER)) |
| :--- |
| [1,2,3] |
{% endraw %}

**Example**
{% raw %}
The following example shows that if the input array has at least one `NULL` value, then the output array will contain a single `NULL` value:

``` sql
SELECT ARRAY_DISTINCT([1, 2, 3, NULL, 1, 2, 3, NULL]) AS res;
```

**Returns**

| res (ARRAY(INTEGER)) |
| :--- |
| [1,2,3,NULL] |
{% endraw %}