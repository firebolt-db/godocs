``` sql
CREATE TABLE exams (grade double precision);
INSERT INTO exams VALUES (1.0), (1.3), (1.3), (2.0), (2.3);
```

Calculate the sample variance of the grades and round to 3 decimal places.
``` sql
SELECT ROUND(VAR_SAMP(grade), 3) as variance from exams;
```

| variance (DOUBLE) |
| :--- |
| 0.297 |