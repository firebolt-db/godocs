The following example normalizes the word 'München' using the Latin-ASCII transliterate ID:
{% include query-window.html sql_file="sql_examples/icu_normalize_example_1.sql" %}

The following example applies a similar operation to the [UPPER](../../../sql_reference/functions-reference/string/upper.html) function:
{% include query-window.html sql_file="sql_examples/icu_normalize_example_2.sql" %}

The function only works for a valid ICU transliterate ID:
{% include query-window.html sql_file="sql_examples/icu_normalize_example_3.sql" %}