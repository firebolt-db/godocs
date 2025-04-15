The following example trims the character `x` from both sides of a string:
``` sql
SELECT BTRIM('xxThe Acceleration Cupxxx', 'x') as result
```

| result (TEXT) |
| :--- |
| 'The Acceleration Cup' |

The following example trims the characters `x` and `y` from both sides of a string. Note that the ordering of characters in `<trim_characters>` is irrelevant:
``` sql
SELECT BTRIM('xyxyThe Acceleration Cupyyxx', 'xy') as result;
```

| result (TEXT) |
| :--- |
| 'The Acceleration Cup' |

The following example omits the <trim_characters> parameter, and thus trims whitespace from both sides of a string:
``` sql
SELECT BTRIM('   The Acceleration Cup     ') as result;
```

| result (TEXT) |
| :--- |
| 'The Acceleration Cup' |