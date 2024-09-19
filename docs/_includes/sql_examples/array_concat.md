{% raw %}
The following example concatenates two integer arrays:
``` sql
SELECT ARRAY_CONCAT([1, 2, 3, 4], [5, 6, 7, 8, 9, 10]) as res;
```

| res (ARRAY(INTEGER)) |
| :--- |
| {1,2,3,4,5,6,7,8,9,10} |
{% endraw %}

{% raw %}
NULLs are retained in the concatenated arrays:
``` sql
SELECT ARRAY_CONCAT([1, 2, NULL, NULL], [NULL, 6]) as res;
```

| res (ARRAY(INTEGER)) |
| :--- |
| {1,2,NULL,NULL,NULL,6} |
{% endraw %}

{% raw %}
The following example concatenates an untyped literal that can be converted to an integer array with an integer array literal:
``` sql
SELECT '{2}' || [1] as res;
```

| res (ARRAY(INTEGER)) |
| :--- |
| {2,1} |
{% endraw %}

{% raw %}
If the array arguments have a different member type, they are casted to their common type:
``` sql
SELECT [1.333] || [1] as res;
```

| res (ARRAY(DOUBLE)) |
| :--- |
| {1.333,1} |
{% endraw %}
