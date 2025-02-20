The following example returns the logarithm of 64.0 to base 2:

{% include query-window.html sql_file="sql_examples/log_example_0.sql" %}

The following example returns the logarithm of 100.0 to the default base 10:

{% include query-window.html sql_file="sql_examples/log_example_1.sql" %}

The logarithm can only be computed for values that are larger than 0. All the following functions return an error:

{% include query-window.html sql_file="sql_examples/log_example_2.sql" %}

When a base is provided, it needs to be positive and not equal to zero. All the following functions return an error:

{% include query-window.html sql_file="sql_examples/log_example_3.sql" %}

