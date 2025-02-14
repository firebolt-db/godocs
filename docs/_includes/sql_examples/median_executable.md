**Example**

The following query uses `UNNEST` to convert an array [1,2,5] into a column, calculates the median value, and returns it as `result`:


{% include query-window.html sql_file="sql_examples/median_example_0.sql" %}

**Returns**

The previous code example returns the middle element as the median because the number of elements in the array is odd.

**Example**

The following query uses `UNNEST` to convert an array [100, NULL, 1, 2, 5] into a column, calculates the median value, and returns it as `result`:

{% include query-window.html sql_file="sql_examples/median_example_1.sql" %}

**Returns**

The previous code example returns the average of the two middle elements after sorting the values, because the number of non-`NULL` elements is even after ignoring `NULL` values. The average of the middle elements, `2` and `5`,  is calculated as : `((2+5)/2)`.

{% include query-window.html sql_file="sql_examples/median_example_2.sql" %}

