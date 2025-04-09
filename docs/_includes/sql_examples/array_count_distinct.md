**Example**
{% raw %}
The following example counts the number of distinct values in the specified array:

``` sql
SELECT ARRAY_COUNT_DISTINCT([1, 2, 3]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 3 |
{% endraw %}

**Example**
{% raw %}
The following example shows that `NULL` values do not contribute to the distinct count:

``` sql
SELECT ARRAY_COUNT_DISTINCT([1, NULL, 2, NULL, 3]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 3 |
{% endraw %}

**Example**
{% raw %}
The following example shows that adding duplicate values does not contribute to the distinct count:

``` sql
SELECT ARRAY_COUNT_DISTINCT([1, NULL, 2, NULL, 3, 1, 2, 3]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 3 |
{% endraw %}
