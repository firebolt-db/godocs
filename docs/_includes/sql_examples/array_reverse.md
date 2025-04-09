**Example**
{% raw %}
The following example returns the reverse of the input array:

``` sql
SELECT ARRAY_REVERSE([1, 2, NULL, 3, 6]) as res;
```
**Returns**

| res (ARRAY(INTEGER)) |
| :--- |
| [6,3,NULL,2,1] |
{% endraw %}

**Example**
{% raw %}
The following example shows that for nested arrays, `ARRAY_REVERSE` only reverses the elements in the outermost array, while preserving the order in the innermost arrays:

``` sql
SELECT ARRAY_REVERSE([[1,2,3], [4,5], NULL, [7], [8,9]]) as res;
```

**Returns**

| res (ARRAY(ARRAY(INTEGER))) |
| :--- |
| [[8,9],[7],NULL,[4,5],[1,2,3]] |
{% endraw %}