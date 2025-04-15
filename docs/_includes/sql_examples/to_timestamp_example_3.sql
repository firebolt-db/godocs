SELECT
    TO_TIMESTAMP(
        'h:19 m:34 s:29 ms:035 us:000123',
        'X:hh24 X:mi X:ss XX:ms XX:us'
    ) as ts;