The following example returns the nearest whole number smaller than 2.5549900:
``` sql
SELECT FLOOR(2.5549900);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 2 |

The following example calculates the nearest whole number smaller than 213.1549, and returns a result of type NUMERIC(20,4), which allows for a total of 20 digits, with 4 values allowed after the decimal point:
``` sql
SELECT FLOOR('213.1549'::NUMERIC(20,4));
```

| ?column? (NUMERIC(20, 4)) |
| :--- |
| 213.0000 |

The following code example rounds the number 2.5549900 down to the second decimal place.
It returns 2.55 because the second parameter 2 specifies rounding to the second digit after the decimal, which corresponds to the hundredths place.
``` sql
SELECT FLOOR(2.5549900, 2);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 2.55 |

The following example calculates the nearest whole number smaller than 1998 that is a multiple of 1000.
It returns 1000 because the second parameter -3 specifies rounding to the third digit before the decimal point, which corresponds to the thousands place.
``` sql
SELECT FLOOR(1998, -3);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 1000 |