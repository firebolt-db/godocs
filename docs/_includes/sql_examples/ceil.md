The following example returns the nearest whole number larger than 2.5549900:
``` sql
SELECT CEIL(2.5549900);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 3 |

The following example calculates the nearest whole number larger than 213.1549, and returns a result of type NUMERIC(20,4), which allows for a total of 20 digits, with 4 values allowed after the decimal point:
``` sql
SELECT CEIL('213.1549'::NUMERIC(20,4));
```

| ?column? (NUMERIC(20, 4)) |
| :--- |
| 214.0000 |

The following example rounds the number 2.5549900 up to the second decimal place.
It returns 2.56 because the second parameter 2 specifies rounding to the second digit after the decimal, which corresponds to the hundredths place.
``` sql
SELECT CEIL(2.5549900, 2);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 2.56 |

The following example calculates the nearest whole number greater than 1998 that is a multiple of 1000.
It returns 2000 because the second parameter -3 specifies rounding to the third digit before the decimal point, which corresponds to the thousands place.
``` sql
SELECT CEIL(1998, -3);
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 2000 |