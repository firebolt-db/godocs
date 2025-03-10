CREATE TABLE sketch_of_data_to_count AS
SELECT hll_count_build(a) a
FROM data_to_count;