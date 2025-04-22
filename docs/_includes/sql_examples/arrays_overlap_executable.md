The following example returns `TRUE` because all input arrays contain the element `2`.

{% include query-window.html sql_file="sql_examples/arrays_overlap_example_0.sql" %}

The following example returns `FALSE` because no element appears in all input arrays.

{% include query-window.html sql_file="sql_examples/arrays_overlap_example_1.sql" %}

The following example returns `FALSE` because no non-`NULL` element appears in all input arrays.

{% include query-window.html sql_file="sql_examples/arrays_overlap_example_2.sql" %}

The following example returns `NULL` because one of the inputs is `NULL`.

{% include query-window.html sql_file="sql_examples/arrays_overlap_example_3.sql" %}

