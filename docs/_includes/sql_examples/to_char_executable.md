The example below outputs the current local time in a formatted string.
Note that the `"` around the words `Date` and `Time` are required, otherwise
the characters `D` and `I` would be interpreted as valid patterns which would
result in the output `6ate` and `T3me`.

{% include query-window.html sql_file="sql_examples/to_char_example_0.sql" %}

The following example outputs the current date in a formatted string with
any time field set to `0` which indicates midnight. Note the quotation marks
again that are required to prevent unintended replacements:

{% include query-window.html sql_file="sql_examples/to_char_example_1.sql" %}

