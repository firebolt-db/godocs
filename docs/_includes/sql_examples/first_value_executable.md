**Example**

The following query uses `UNNEST` to convert an array `[1,2,5]` into a column, order the values, and returns the first value as `result`:


{% include query-window.html sql_file="sql_examples/first_value_example_0.sql" %}

**Returns**

The previous code example returns the first element after ordering.

**Example**

The following query uses `UNNEST` to convert an array `[100, NULL, 1]` into a column, order the values, and returns the first value as `result`:


{% include query-window.html sql_file="sql_examples/first_value_example_1.sql" %}

**Returns**

The previous code example returns `NULL` values because `ORDER BY` specifies 'nulls first'.

{% include query-window.html sql_file="sql_examples/first_value_example_2.sql" %}

