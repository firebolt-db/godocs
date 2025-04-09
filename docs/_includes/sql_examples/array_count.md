**Example**
{% raw %}
The following example searches through the specified array for any elements that are greater than three:

``` sql
SELECT ARRAY_COUNT(x -> x > 3, [ 1, 2, 3, 9, NULL ]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 1 |
{% endraw %}

In the previous example, only one number in the array is greater than three, as specified in `<function>`.

**Example**
{% raw %}
In the following example, no `<function>` provided, so `ARRAY_COUNT` counts all four of the elements in the array that evaluate to `TRUE`:

``` sql
SELECT ARRAY_COUNT([TRUE, FALSE, 2::BOOLEAN, 3 IS NOT NULL, NULL IS NULL, NULL]) AS res;
```

**Returns**

| res (INTEGER) |
| :--- |
| 4 |
{% endraw %}

In the previous example, all elements except `FALSE` and `NULL` evaluate to `TRUE`.