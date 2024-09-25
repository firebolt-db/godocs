``` sql
CREATE TABLE exams (grade double precision);
INSERT INTO exams VALUES (1.0), (1.3), (1.3), (2.0), (2.3);
```

Calculate the population standard deviation of the grades and round to 3 decimal digits.
``` sql
SELECT ROUND(STDDEV_POP(grade), 3) as stddev from exams;
```

| stddev (DOUBLE) |
| :--- |
| 0.487 |