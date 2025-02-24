The following example returns an array with values one to four:

{% include query-window.html sql_file="sql_examples/array_enumerate_example_0.sql" %}

The array passed to the function can contain arbitrary types:

{% include query-window.html sql_file="sql_examples/array_enumerate_example_1.sql" %}

NULL values are still reflected in the returned result:

{% include query-window.html sql_file="sql_examples/array_enumerate_example_2.sql" %}

If the array passed to the function is NULL, so is the result:

{% include query-window.html sql_file="sql_examples/array_enumerate_example_3.sql" %}

