**Example**

{% raw %}
The following example concatenates two integer arrays into one:

``` sql
SELECT ARRAY_CONCAT([1, 2, 3, 4], [5, 6, 7, 8, 9, 10]) as res;
```

**Returns**

| res (ARRAY(INTEGER)) |
| :--- |
| [1,2,3,4,5,6,7,8,9,10] |
{% endraw %}

**Example**
{% raw %}
The following example concatenates two arrays that contain `NULL` values into a single array, preserving the `NULL` elements:

``` sql
SELECT ARRAY_CONCAT([1, 2, NULL, NULL], [NULL, 6]) as res;
```

**Returns**

| res (ARRAY(INTEGER)) |
| :--- |
| [1,2,NULL,NULL,NULL,6] |
{% endraw %}

**Example**
{% raw %}
The following example concatenates an untyped literal, which is a value without a defined data type that can be converted to an integer array, with an integer array literal:

``` sql
SELECT '{2}' || [1] as res;
```

**Returns**

| res (ARRAY(INTEGER)) |
| :--- |
| [2,1] |
{% endraw %}

**Example**
{% raw %}
If the array arguments have different data types, they are automatically cast to a common type during concatenation. The following example concatenates an array containing an [INTEGER](https://docs.firebolt.io/sql_reference/data-types.html#integer) and a [DOUBLE](https://docs.firebolt.io/sql_reference/data-types.html#double-precision):

``` sql
SELECT [1.333] || [1] as res;
```

**Returns**

| res (ARRAY(DOUBLE)) |
| :--- |
| [1.333,1] |
{% endraw %}
