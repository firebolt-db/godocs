``` sql
CREATE TABLE exams (grade double precision);
INSERT INTO exams VALUES (1.0), (1.3), (1.3), (2.0), (2.3);
```

``` sql
SELECT VAR_SAMP(grade) as result from exams;
```

| result (DOUBLE) |
| :--- |
| 0.2970000000000006 |