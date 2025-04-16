In the following example, the only element shared between all three arrays is the `1`:

{% include query-window.html sql_file="sql_examples/array_intersect_example_0.sql" %}

Passing in one argument array is allowed:

{% include query-window.html sql_file="sql_examples/array_intersect_example_1.sql" %}

In the following example, `ARRAY_SORT` is used to ensure the results are in ascending order:

{% include query-window.html sql_file="sql_examples/array_intersect_example_2.sql" %}

`NULL` can appear in the intersection, only if it appears in all the argument arrays:

{% include query-window.html sql_file="sql_examples/array_intersect_example_3.sql" %}

The result does not contain duplicates, even if the same value appears multiple times in all argument arrays:

{% include query-window.html sql_file="sql_examples/array_intersect_example_4.sql" %}

Arbitrarily nested arrays are also supported:

{% include query-window.html sql_file="sql_examples/array_intersect_example_5.sql" %}

