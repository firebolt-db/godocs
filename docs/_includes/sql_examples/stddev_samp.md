The following code creates an `exams` table with a `grade` column of type `DOUBLE PRECISION`, and inserts five grade values into it:

``` sql
CREATE TABLE exams (grade DOUBLE PRECISION);
INSERT INTO exams VALUES (4.0), (3.7), (3.3), (2.7), (2.7);
```

The following code calculates the sample standard deviation of the grade values from the `exams` table, rounds the result to three decimal places, and returns it as `stddev`:

``` sql
SELECT ROUND(STDDEV_SAMP(grade), 3) as stddev from exams;
```

**Returns**
The previous code returns the following result:

| stddev (DOUBLE PRECISION) |
| :--- |
| 0.585 |