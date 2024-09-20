**Example**
{% raw %}
The following example sorts the array in descending order, with `NULL` values always placed at the end:

``` sql
SELECT ARRAY_REVERSE_SORT([4, 1, NULL, 3, 2]);
```

**Returns**

| ?column? (ARRAY(INTEGER)) |
| :--- |
| [4,3,2,1,NULL] |
{% endraw %}

**Example**
{% raw %}
In the following example, the modulus operator (`%`) calculates the remainder for each number when divided by two. `ARRAY_REVERSE_SORT` then sorts the numbers based on that remainder. It places odd numbers, which have a remainder of one, before even numbers, which have a remainder of zero.

``` sql
SELECT ARRAY_REVERSE_SORT(x -> x % 2, [4, 1, 3, 2]);
```

**Returns**

| ?column? (ARRAY(INTEGER)) |
| :--- |
| [1,3,4,2] |
{% endraw %}