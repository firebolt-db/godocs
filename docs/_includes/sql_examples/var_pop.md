``` sql
CREATE TABLE exams (grade double precision);
INSERT INTO exams VALUES (1.0), (1.3), (1.3), (2.0), (2.3);
```

``` sql
SELECT VAR_POP(grade) as result from exams;
```

| result (DOUBLE) |
| :--- |
| 0.23760000000000048 |