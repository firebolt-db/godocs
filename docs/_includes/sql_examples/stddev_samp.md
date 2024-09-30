``` sql
CREATE TABLE exams (grade DOUBLE PRECISION);
INSERT INTO exams VALUES (4.0), (3.7), (3.3), (2.7), (2.7);
```

Calculate the sample standard deviation of the grades and round to 3 decimal digits.
``` sql
SELECT ROUND(STDDEV_SAMP(grade), 3) as stddev from exams;
```

| stddev (DOUBLE PRECISION) |
| :--- |
| 0.585 |