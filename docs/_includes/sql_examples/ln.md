The following example computes the natural logarithm of 1.0:
``` sql
SELECT LN(1.0);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 0 |

The following example returns the natural logarithm close to e:
``` sql
SELECT LN(2.7182818284590452353);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 1 |

The natural logarithm can only be computed for values that are larger than 0. All the following functions return an error:
``` sql
SELECT LN(0.0);
-- SELECT LN(-1.0);
-- SELECT LN('-Inf');
```

ERROR: Line 1, Column 8: Cannot take the logarithm of 0. The argument needs to be larger than 0.
