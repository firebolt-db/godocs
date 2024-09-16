{% raw %}
The function simply counts the number of elements in the outer array, including `NULLs`:
``` sql
SELECT ARRAY_LENGTH([1, 2, 3, 4, NULL]) AS res;
```

| res (INTEGER) |
| :--- |
| 5 |
{% endraw %}

{% raw %}
Duplicate values increase the count:
``` sql
SELECT ARRAY_LENGTH([1, 2, 3, 4, NULL, 1, 2, 3, 4, NULL]) AS res;
```

| res (INTEGER) |
| :--- |
| 10 |
{% endraw %}

{% raw %}
For nested arrays, only the length of the outermost array matters:
``` sql
SELECT ARRAY_LENGTH([[1, 2, 3], [4, 5, 6, 7]]) AS res;
```

| res (INTEGER) |
| :--- |
| 2 |
{% endraw %}