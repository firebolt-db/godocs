``` sql
CREATE TABLE exams (grade double precision);
INSERT INTO exams VALUES (4.0), (3.7), (3.3), (2.7), (2.7);
```

Calculate the sample variance of the grades and round to 3 decimal places.
``` sql
SELECT ROUND(VAR_SAMP(grade), 3) as variance from exams;
```

| variance (DOUBLE PRECISION) |
| :--- |
| 0.342 |