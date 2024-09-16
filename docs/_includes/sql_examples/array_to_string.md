{% raw %}
In the example below, the three elements are concatenated with no delimiter.
``` sql
SELECT ARRAY_TO_STRING(['1', '2', '3']) AS levels;
```

| levels (TEXT) |
| :--- |
| '123' |
{% endraw %}

{% raw %}
`NULL` values are ignored by `ARRAY_TO_STRING`:
``` sql
SELECT ARRAY_TO_STRING(['1', NULL, '2', NULL, '3', NULL]) AS levels;
```

| levels (TEXT) |
| :--- |
| '123' |
{% endraw %}

{% raw %}
In this example below, the elements are concatenated separated by a comma.
``` sql
SELECT ARRAY_TO_STRING(['1', '2', '3'], ',') AS levels;
```

| levels (TEXT) |
| :--- |
| '1,2,3' |
{% endraw %}

{% raw %}
In this example below, the elements of a nested array containing a NULL are concatenated.
``` sql
SELECT ARRAY_TO_STRING([[1, 2], [3, 4], [NULL, 5]], ',') AS levels;
```

| levels (TEXT) |
| :--- |
| '1,2,3,4,5' |
{% endraw %}