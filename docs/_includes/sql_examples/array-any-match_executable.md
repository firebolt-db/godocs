**Example**
The following code example checks if an array contains the value `esimpson` as the result `is_he_playing`:

{% include query-window.html sql_file="sql_examples/array-any-match_example_0.sql" %}

**Returns**
The previous code returns `FALSE` because the array does not contain the specified value:

**Example**
The following code example checks if each element in the first array is divisible by the corresponding element in the second array in a result labeled `divisible`:

{% include query-window.html sql_file="sql_examples/array-any-match_example_1.sql" %}

**Returns**
The previous code returns `TRUE` because each element in the first array is divisible by its corresponding element in the second array:

**Example**
The following code example evaluates multiple arrays using `ARRAY_ANY_MATCH`:

{% include query-window.html sql_file="sql_examples/array-any-match_example_2.sql" %}

**Returns**
The previous code returns `FALSE` for the empty array, `TRUE` for the `[TRUE]` array, `FALSE` for the `[FALSE]` array, `NULL` for the `[NULL]` array, and `FALSE` for the `[FALSE, NULL]` array:

