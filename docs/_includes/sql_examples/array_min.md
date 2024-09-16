{% raw %}
The following example calculates the minimum number in the array:
``` sql
SELECT ARRAY_MIN([1, 2, 3, 4]) AS res;
```

| res (INTEGER) |
| :--- |
| 1 |
{% endraw %}

{% raw %}
This also works when the array contains `NULLs`:
``` sql
SELECT ARRAY_MIN([1, NULL, 2, NULL, 3, NULL, 4, NULL]) AS res;
```

| res (INTEGER) |
| :--- |
| 1 |
{% endraw %}

{% raw %}
For empty arrays and arrays that only contain `NULL`, the `ARRAY_MIN` function will return `NULL`:
``` sql
SELECT ARRAY_MIN([]) as res1, ARRAY_MIN([NULL]) AS res2;
```

| res1 (TEXT) | res2 (TEXT) |
| :--- | :--- |
| NULL,NULL |
{% endraw %}