**Example**
{% raw %}
The following example sorts the array in ascending order, with `NULL` values always placed at the end:

``` sql
SELECT ARRAY_SORT([4, 1, NULL, 3, 2]);
```

**Returns**

| ?column? (ARRAY(INTEGER)) |
| :--- |
| [1,2,3,4,NULL] |
{% endraw %}

**Example**
{% raw %}
In the following example, the modulus operator (`%`) calculates the remainder for each number when divided by two. `ARRAY_SORT` then sorts the numbers based on that remainder. It places even numbers, which have a remainder of zero, before odd numbers, which have a remainder of one:

``` sql
SELECT ARRAY_SORT(x -> x % 2, [4, 1, 3, 2]);
```

**Returns**

| ?column? (ARRAY(INTEGER)) |
| :--- |
| [4,2,1,3] |
{% endraw %}