WITH data as (
    select '1597-12-03 13:49:30.511757+00'::timestamptz as ts 
)
SELECT
    ts as original_ts,
    FROM_UNIXTIME(
        extract(epoch from ts)
    ) as converted_ts
FROM data