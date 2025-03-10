**Example**

The following code example shifts `0001`, the binary representation of `1`, to the right by two bits, which yields `0000`, the binary representation for `0`:


{% include query-window.html sql_file="sql_examples/bit_shift_right_example_0.sql" %}

**Example**

The following code example shifts `00101`, the binary representation of `5`, to the right by two bits, which yields `00001`, the binary representation for `1`:


{% include query-window.html sql_file="sql_examples/bit_shift_right_example_1.sql" %}

**Example**

The following code example shifts the binary representation of `-3`, which is `1111111111111101` in signed two's complement, one bit to the right, resulting in `1111111111111110`, the signed two's complement of `-2`:


{% include query-window.html sql_file="sql_examples/bit_shift_right_example_2.sql" %}

