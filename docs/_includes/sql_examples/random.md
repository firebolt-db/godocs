The following code example demonstrates using RANDOM without any other numeric functions. This generates a DOUBLE PRECISION value less than 1:
``` sql
SELECT RANDOM()
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 0.901744181467958 |

To create a random integer number between two values, you can use RANDOM with the FLOOR function. If a is the lesser value and b is the greater value,
compute `FLOOR(RANDOM() * (b - a + 1)) + a`.
The following code example generates a random integer between 50 and 100:
``` sql
SELECT (RANDOM() * (100 - 50 + 1)) + 50
```

| ?column? (DOUBLE PRECISION) |
| :--- |
| 79.86234094408863 |