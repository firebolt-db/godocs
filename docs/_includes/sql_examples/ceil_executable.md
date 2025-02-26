The following example returns the nearest whole number larger than `2.5549900`:

{% include query-window.html sql_file="sql_examples/ceil_example_0.sql" %}

The following example calculates the nearest whole number larger than `213.1549`, and returns a result of type `NUMERIC(20,4)`, which allows for a total of 20 digits, with 4 values allowed after the decimal point:

{% include query-window.html sql_file="sql_examples/ceil_example_1.sql" %}

The following example rounds the number `2.5549900` up to the second decimal place.
It returns `2.56` because the second parameter 2 specifies rounding to the second digit after the decimal, which corresponds to the hundredths place.

{% include query-window.html sql_file="sql_examples/ceil_example_2.sql" %}

The following example calculates the nearest whole number greater than `1998` that is a multiple of `1000`.
It returns `2000` because the second parameter -3 specifies rounding to the third digit before the decimal point, which corresponds to the thousands place.

{% include query-window.html sql_file="sql_examples/ceil_example_3.sql" %}

