INSERT INTO sketch_of_data_to_count
SELECT hll_count_build(a)
FROM data_to_count2;