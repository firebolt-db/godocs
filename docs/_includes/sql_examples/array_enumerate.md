The following example returns an array with values one to four:
``` sql
SELECT ARRAY_ENUMERATE([7, 9, 3, 4]) AS one_to_four;
```

| one_to_four (ARRAY(INTEGER)) |
| :--- |
| {1,2,3,4} |

The array passed to the function can contain arbitrary types:
``` sql
SELECT ARRAY_ENUMERATE(['hello', 'world']) AS one_to_two;
```

| one_to_two (ARRAY(INTEGER)) |
| :--- |
| {1,2} |

`NULL` values are still reflected in the returned result:
``` sql
SELECT ARRAY_ENUMERATE([7, NULL, 3, NULL]) AS one_to_four;
```

| one_to_four (ARRAY(INTEGER)) |
| :--- |
| {1,2,3,4} |

If the array passed to the function is `NULL`, so is the result:
``` sql
SELECT ARRAY_ENUMERATE(NULL) AS null_result;
```

| null_result (ARRAY(INTEGER)) |
| :--- |
| NULL |