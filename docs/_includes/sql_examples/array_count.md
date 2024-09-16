{% raw %}
The example below searches through the array for any elements that are greater than 3. Only one number that matches this criteria is found, so the function returns 1
``` sql
SELECT ARRAY_COUNT(x -> x > 3, [ 1, 2, 3, 9, NULL ]) AS res;
```

| res (INTEGER) |
| :--- |
| 1 |
{% endraw %}

{% raw %}
In the example below, there is no `<function>` provided in the `ARRAY_COUNT` function. This means the function will count all of the elements in the array that evaluate to `TRUE`. Below, this is the case for all values except `FALSE` and `null`:
``` sql
SELECT ARRAY_COUNT([TRUE, FALSE, 2::BOOLEAN, 3 is not null, null is null, null]) AS res;
```

| res (INTEGER) |
| :--- |
| 4 |
{% endraw %}