At nesting level two, the result array will be flat:
``` sql
SELECT ARRAY_FLATTEN([[1, 2], [NULL, 3], [3, 4]]) as res;
```

| res (ARRAY(INTEGER)) |
| :--- |
| {1,2,NULL,3,3,4} |

At nesting level three, the result array will have nesting level two:
``` sql
SELECT ARRAY_FLATTEN([[[1, 2]], [[NULL, 3], [3, 4]]]) as res;
```

| res (ARRAY(ARRAY(INTEGER))) |
| :--- |
| {{1,2},{NULL,3},{3,4}} |

The function does not work when the array is already flat:
``` sql
SELECT ARRAY_FLATTEN([1, 2, NULL, 3, 3, 4]) as res;
```
```
ERROR: Line 1, Column 8: function signature 'array_flatten(array(integer))' not found, supported signatures are array_flatten(array(array))
```