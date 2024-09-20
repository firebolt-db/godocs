**Example**
{% raw %}
The following example checks if the element `danielle53` is part of the specified array:

``` sql
SELECT ARRAY_CONTAINS(['sabrina21', 'rileyjon', 'ywilson', 'danielle53', NULL], 'danielle53') as res;
```

 **Returns**

| res (BOOLEAN) |
| :--- |
| true |
{% endraw %}

**Example**
{% raw %}
The following example checks if the element `danielle53` is part of the specified array:

``` sql
SELECT ARRAY_CONTAINS(['sabrina21', 'rileyjon', 'ywilson', NULL] , 'danielle53') as res;
```

**Returns**

| res (BOOLEAN) |
| :--- |
| false |
{% endraw %}

**Example**
{% raw %}
The following example checks if `NULL` is present in a different array than the previous example:

``` sql
SELECT ARRAY_CONTAINS(['sabrina21', 'rileyjon', 'ywilson', NULL] , NULL) as res;
```
**Returns**

| res (BOOLEAN) |
| :--- |
| true |
{% endraw %}

The previous example returns `TRUE` because `ARRAY_CONTAINS` uses `IS NOT DISTINCT FROM` semantics. This means `NULL` is treated as a valid value, and `NULL = NULL` returns `TRUE`.