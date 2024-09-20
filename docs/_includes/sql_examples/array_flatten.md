**Example**
{% raw %}
The following example flattens an array with two levels of nesting into a single-level flat array:

``` sql
SELECT ARRAY_FLATTEN([[1, 2], [NULL, 3], [3, 4]]) as res;
```

**Returns**

| res (ARRAY(INTEGER)) |
| :--- |
| [1,2,NULL,3,3,4] |
{% endraw %}

**Example**
{% raw %}
The following example flattens an array with three levels of nesting into an array with two levels of nesting:

``` sql
SELECT ARRAY_FLATTEN([[[1, 2]], [[NULL, 3], [3, 4]]]) as res;
```

**Returns**

| res (ARRAY(ARRAY(INTEGER))) |
| :--- |
| [[1,2],[NULL,3],[3,4]] |
{% endraw %}

**Example**
{% raw %}
The following example shows that `ARRAY_FLATTEN` does not flatten an array that is already flat:

``` sql
SELECT ARRAY_FLATTEN([1, 2, NULL, 3, 3, 4]) as res;
```

**Returns**

```
ERROR: Line 1, Column 8: function signature 'array_flatten(array(integer))' not found, supported signatures are array_flatten(array(array))
```
{% endraw %}