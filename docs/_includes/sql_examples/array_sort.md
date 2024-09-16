{% raw %}
The following example sorts the array in an ascending way, `NULLS` are always placed last:
``` sql
SELECT ARRAY_SORT([4, 1, NULL, 3, 2]);
```

| ?column? (ARRAY(INTEGER)) |
| :--- |
| {1,2,3,4,NULL} |
{% endraw %}

{% raw %}
In the example below, the modulus operator is used to calculate the remainder on any odd numbers. Therefore `ARRAY_SORT` puts the lower (even) numbers first in the results.
``` sql
SELECT ARRAY_SORT(x -> x % 2, [4, 1, 3, 2]);
```

| ?column? (ARRAY(INTEGER)) |
| :--- |
| {4,2,1,3} |
{% endraw %}