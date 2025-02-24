The following code example demonstrates using `RANDOM` without any other numeric functions. This generates a `DOUBLE PRECISION` value less than 1:

{% include query-window.html sql_file="sql_examples/random_example_0.sql" %}

To create a random integer number between two values, you can use `RANDOM` with the `FLOOR` function. If `a` is the lesser value and `b` is the greater value,
compute `FLOOR(RANDOM() * (b - a + 1)) + a`.
The following code example generates a random integer between 50 and 100:

{% include query-window.html sql_file="sql_examples/random_example_1.sql" %}

