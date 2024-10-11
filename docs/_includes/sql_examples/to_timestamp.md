The example below shows our separators and non-separators can cause skips. The separator `' '` (space) in the `<format>` matches the other separator `'/'` in the `<expression>`.
The non-separator `'x'` will match any other character, in this case the `'a'`. Lastly, the two separators `'++'` will match up to two other separators,
here the first `'x'` matches `'.'` while the second `'x'` will simply be ignored as no other separators follow.
``` sql
SELECT
TO_TIMESTAMP(
'2023/aJUN.23',
'YYYY xMON++DD'
) as ts;
```

| ts (TIMESTAMPTZ) |
| :--- |
| '2023-06-23 00:00:00+00' |

The example below shows how the year is adjusted to be nearest to 2020 because `YYY` was used to match a less than four digit number. To receive the exact year `'180'` use `YYYY` instead.
Furthermore, as the three separators are quotes `"..."` they will match any character (separator or non-separator) which in this case is `'ar '`.
``` sql
SELECT
TO_TIMESTAMP(
'Year 180: August 4th',
'xx"..."yyy: month DDxx'
) as ts;
```

| ts (TIMESTAMPTZ) |
| :--- |
| '2180-08-04 00:00:00+00' |

``` sql
SELECT
TO_TIMESTAMP(
'Date: August 2nd, 2023 at 3pm +2',
'Xxxx: month DDxx, YYYY at HH12am TZH'
) as ts;
```

| ts (TIMESTAMPTZ) |
| :--- |
| '2023-08-02 13:00:00+00' |

``` sql
SELECT
TO_TIMESTAMP(
'h:19 m:34 s:29 ms:035 us:000123',
'X:hh24 X:mi X:ss XX:ms XX:us'
) as ts;
```

| ts (TIMESTAMPTZ) |
| :--- |
| '0001-01-01 19:34:29.035123+00' |

``` sql
SELECT
FROM_UNIXTIME(
1728053781.761451
) as ts;
```

| ts (TIMESTAMPTZ) |
| :--- |
| '2024-10-04 14:56:21.761451+00' |

Due to rounding it can happen that the conversion from an extracted epoch back to a timestamp does not generate the original timestamp.
``` sql
WITH data as (
select '1597-12-03 13:49:30.511757+00'::timestamptz as ts
)
SELECT
ts as original_ts,
FROM_UNIXTIME(
extract(epoch from ts)
) as converted_ts
FROM data
```

| original_ts (TIMESTAMPTZ) | converted_ts (TIMESTAMPTZ) |
| :--- | :--- |
| '1597-12-03 13:49:30.511757+00' | '1597-12-03 13:49:30.511756+00' |