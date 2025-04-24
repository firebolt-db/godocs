The following example generates 2-grams (bigrams) from the string 'hello world':

{% include query-window.html sql_file="sql_examples/ngram_example_0.sql" %}

The following example generates 3-grams (trigrams) from the string 'hello world':

{% include query-window.html sql_file="sql_examples/ngram_example_1.sql" %}

The following example generates 1-grams (unigrams) from the string 'hello':

{% include query-window.html sql_file="sql_examples/ngram_example_2.sql" %}

The following example generates 10-grams from the string 'hi'. Since the string length matches the n-gram size, the result contains the entire string:

{% include query-window.html sql_file="sql_examples/ngram_example_3.sql" %}

The following example uses an n-gram size of 0, which is invalid and throws an error:

{% include query-window.html sql_file="sql_examples/ngram_example_4.sql" %}

The following example uses a negative n-gram size, which is invalid and throws an error:

{% include query-window.html sql_file="sql_examples/ngram_example_5.sql" %}

The following example generates 2-grams (bigrams) from the Japanese string 'こんにちは':

{% include query-window.html sql_file="sql_examples/ngram_example_6.sql" %}

The following example generates 2-grams (bigrams) from the string of emojis '😊👍🎉':

{% include query-window.html sql_file="sql_examples/ngram_example_7.sql" %}

