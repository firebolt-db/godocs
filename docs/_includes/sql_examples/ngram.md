The following example generates 2-grams (bigrams) from the string 'hello world':
``` sql
SELECT NGRAM(2, 'hello world') AS result;
```

| result (ARRAY(TEXT)) |
| :--- |
| {he,el,ll,lo,"o "," w",wo,or,rl,ld} |

The following example generates 3-grams (trigrams) from the string 'hello world':
``` sql
SELECT NGRAM(3, 'hello world') AS result;
```

| result (ARRAY(TEXT)) |
| :--- |
| {hel,ell,llo,"lo ","o w"," wo",wor,orl,rld} |

The following example generates 1-grams (unigrams) from the string 'hello':
``` sql
SELECT NGRAM(1, 'hello') AS result;
```

| result (ARRAY(TEXT)) |
| :--- |
| {h,e,l,l,o} |

The following example generates 10-grams from the string 'hi'. Since the string length matches the n-gram size, the result contains the entire string:
``` sql
SELECT NGRAM(10, 'hi') AS result;
```

| result (ARRAY(TEXT)) |
| :--- |
| {hi} |

The following example uses an n-gram size of 0, which is invalid and throws an error:
``` sql
SELECT NGRAM(0, 'hi') AS result;
```

ERROR: Line 1, Column 8: Invalid n-gram size: 0. Must be greater than 0. Choose an n-gram size larger than 0 or NULL.


The following example uses a negative n-gram size, which is invalid and throws an error:
``` sql
SELECT NGRAM(-1, 'hi') AS result;
```

ERROR: Line 1, Column 8: Invalid n-gram size: -1. Must be greater than 0. Choose an n-gram size larger than 0 or NULL.


The following example generates 2-grams (bigrams) from the Japanese string 'こんにちは':
``` sql
SELECT NGRAM(2, 'こんにちは') AS result;
```

| result (ARRAY(TEXT)) |
| :--- |
| {こん,んに,にち,ちは} |

The following example generates 2-grams (bigrams) from the string of emojis '😊👍🎉':
``` sql
SELECT NGRAM(2, '😊👍🎉') AS result;
```

| result (ARRAY(TEXT)) |
| :--- |
| {😊👍,👍🎉} |