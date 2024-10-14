The following code example generates a random UUID as a `TEXT` value:
``` sql
SELECT gen_random_uuid_text() as id_col
```

| id_col (TEXT) |
| :--- |
| 'acc612ea-1a7d-4a49-b977-2486c7963d84' |