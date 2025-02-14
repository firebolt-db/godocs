The following example splits the text into an array at the `|` character.
``` sql
SELECT STRING_TO_ARRAY('stephen70|esimpson|ruthgill|', '|') AS nicknames;
```

**Returns**

| nicknames (ARRAY(TEXT)) |
| :--- |
| {stephen70,esimpson,ruthgill,""} |

The following example calls `STRING_TO_ARRAY` with an empty delimiter, resulting in an array of size one containing the input text.
``` sql
SELECT STRING_TO_ARRAY('firebolt', '') as size_one_array;
```

**Returns**

| size_one_array (ARRAY(TEXT)) |
| :--- |
| {firebolt} |

The following example calls `STRING_TO_ARRAY` with `NULL` as the delimiter, resulting in the text being split into separate characters.
``` sql
SELECT STRING_TO_ARRAY('firebolt', NULL) AS single_characters;
```

**Returns**

| single_characters (ARRAY(TEXT)) |
| :--- |
| {f,i,r,e,b,o,l,t} |