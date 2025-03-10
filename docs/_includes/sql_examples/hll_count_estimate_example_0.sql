CREATE TABLE data_to_count AS
SELECT *
FROM generate_series(0, 10000000, 3) a;