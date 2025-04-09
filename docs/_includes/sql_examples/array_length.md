**Example**
{% raw %}
The following example counts the number of elements in the specified array:

``` sql
SELECT ARRAY_LENGTH([1, 2, 3, 4, NULL]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 5 |
{% endraw %}

In the previous code example, `NULL` elements are counted as part of the array.

**Example**
{% raw %}
The following example shows that duplicate values contribute to the total count of the array:

``` sql
SELECT ARRAY_LENGTH([1, 2, 3, 4, NULL, 1, 2, 3, 4, NULL]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 10 |
{% endraw %}

**Example**
{% raw %}
The following example calculates the length of a nested array:

``` sql
SELECT ARRAY_LENGTH([[1, 2, 3], [4, 5, 6, 7]]) AS res;
```
**Returns**

| res (INTEGER) |
| :--- |
| 2 |
{% endraw %}

In the previous example, `ARRAY_LENGTH` only counts the elements in the outermost array.