{% raw %}
This returns true since 'danielle53' is part of the array:
``` sql
SELECT ARRAY_CONTAINS(['sabrina21', 'rileyjon', 'ywilson', 'danielle53', NULL], 'danielle53') as res;
```

| res (BOOLEAN) |
| :--- |
| t |
{% endraw %}

{% raw %}
This returns false since 'danielle53' is not part of the array:
``` sql
SELECT ARRAY_CONTAINS(['sabrina21', 'rileyjon', 'ywilson', NULL] , 'danielle53') as res;
```

| res (BOOLEAN) |
| :--- |
| f |
{% endraw %}

{% raw %}
When looking for NULL, returns true if the array contains a NULL.
This is because `ARRAY_CONTAINS` implements `IS NOT DISTINCT FROM` semantics:
``` sql
SELECT ARRAY_CONTAINS(['sabrina21', 'rileyjon', 'ywilson', NULL] , NULL) as res;
```

| res (BOOLEAN) |
| :--- |
| t |
{% endraw %}
