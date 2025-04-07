The following example splits the text into an array at the `|` character.

{% include query-window.html sql_file="sql_examples/string_to_array_example_0.sql" %}

**Returns**

The following example calls `STRING_TO_ARRAY` with an empty delimiter, resulting in an array of size one containing the input text.

{% include query-window.html sql_file="sql_examples/string_to_array_example_1.sql" %}

**Returns**

The following example calls `STRING_TO_ARRAY` with `NULL` as the delimiter, resulting in the text being split into separate characters.

{% include query-window.html sql_file="sql_examples/string_to_array_example_2.sql" %}

**Returns**

