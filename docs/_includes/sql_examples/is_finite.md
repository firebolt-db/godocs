The following example checks whether the value inf, after being cast to a `DOUBLE PRECISION` data type, is a finite number:
``` sql
SELECT IS_FINITE('inf'::DOUBLE PRECISION);
```

| ?column? (BOOLEAN) |
| :--- |
| f |

The following code example checks whether the value 10, after being cast to a `REAL` data type, is an infinite number:
``` sql
SELECT IS_FINITE(10::REAL);
```

| ?column? (BOOLEAN) |
| :--- |
| t |