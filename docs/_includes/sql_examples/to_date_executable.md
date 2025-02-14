The following example shows that separators and non-separators can cause skips. The separator `' '` (space) in the `<format>` matches the other separator `'/'` in the `<expression>`. The non-separator `'x'` will match any other character, in this case the `'a'`. Lastly, the two separators `'++'` will match up to two other separators, here the first `'x'` matches `'.'` while the second `'x'` will simply be ignored as no other separators follow.

{% include query-window.html sql_file="sql_examples/to_date_example_0.sql" %}


The following example shows how the year is adjusted to be nearest to 2020 because `YYY` was used to match a number that contains less than four digits. To receive the exact year `'180'` use `YYYY` instead.
Furthermore, as the three separators are quotes `"..."` they will match any character (separator or non-separator) which in this case is `'ar '`.

{% include query-window.html sql_file="sql_examples/to_date_example_1.sql" %}

