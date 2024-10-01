The following code creates an `exams` table with a `grade` column of type `DOUBLE PRECISION`, and inserts five grade values into it:

``` sql
CREATE TABLE exams (grade DOUBLE PRECISION);
INSERT INTO exams VALUES (4.0), (3.7), (3.3), (2.7), (2.7);
```

The following code calculates the population variance of the grade values from the `exams` table, rounds the result to three decimal places, and returns it as `variance`:

``` sql
SELECT ROUND(VAR_POP(grade), 3) as variance from exams;
```

**Returns**
The previous code returns the following result:

| variance (DOUBLE PRECISION) |
| :--- |
| 0.274 |