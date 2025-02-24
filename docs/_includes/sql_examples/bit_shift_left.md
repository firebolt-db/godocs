**Example**

The following code example shifts `0001`, the binary representation of `1`, to the left by two bits, which yields `0100`, the binary representation for `4`:

``` sql
SELECT bit_shift_left(1, 2) AS res;
```

| res (INTEGER) |
| :--- |
| 4 |

**Example**

The following code example shifts `00101`, the binary representation of `5`, to the left by two bits, which yields `10100`, the binary representation of `20`:

``` sql
SELECT bit_shift_left(5, 2) AS res;
```

| res (INTEGER) |
| :--- |
| 20 |

**Example**

The following code example shifts the binary representation of `-3`, which is `1111111111111101` in signed two's complement, one bit to the left, resulting in `1111111111111010`, the binary signed two's complement of `-6`:

``` sql
SELECT bit_shift_left(-3, 1) AS res;
```

| res (INTEGER) |
| :--- |
| -6 |