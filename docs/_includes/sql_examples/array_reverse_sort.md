The following example sorts the array in a descending way, `NULLS` are always placed last:
``` sql
SELECT ARRAY_REVERSE_SORT([4, 1, NULL, 3, 2]);
```

| ?column? (ARRAY(INTEGER)) |
| :--- |
| {4,3,2,1,NULL} |

In the example below, the modulus operator is used to calculate the remainder on any odd numbers. Therefore `ARRAY_REVERSE_SORT` puts the lower (even) numbers last in the results.
``` sql
SELECT ARRAY_REVERSE_SORT(x -> x % 2, [4, 1, 3, 2]);
```

| ?column? (ARRAY(INTEGER)) |
| :--- |
| {1,3,4,2} |