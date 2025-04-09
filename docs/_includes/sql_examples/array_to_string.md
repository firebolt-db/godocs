**Example**
{% raw %}
The following example concatenates three elements without using a delimiter:

``` sql
SELECT ARRAY_TO_STRING(['1', '2', '3']) AS levels;
```

**Returns**

| levels (TEXT) |
| :--- |
| '123' |
{% endraw %}

**Example**
{% raw %}
In the following example, `ARRAY_TO_STRING` ignores `NULL` values when concatenating the array elements:

``` sql
SELECT ARRAY_TO_STRING(['1', NULL, '2', NULL, '3', NULL]) AS levels;
```

**Returns**

| levels (TEXT) |
| :--- |
| '123' |
{% endraw %}


**Example**
{% raw %}
In the following example, the array elements are concatenated with a comma (`,`) as the delimiter:

``` sql
SELECT ARRAY_TO_STRING(['1', '2', '3'], ',') AS levels;
```

**Returns**

| levels (TEXT) |
| :--- |
| '1,2,3' |
{% endraw %}

**Example**
{% raw %}
The following example concatenates the elements of a nested array, skipping the `NULL` value:

``` sql
SELECT ARRAY_TO_STRING([[1, 2], [3, 4], [NULL, 5]], ',') AS levels;
```

**Returns**

| levels (TEXT) |
| :--- |
| '1,2,3,4,5' |
{% endraw %}

In the previous example, `ARRAY_TO_STRING` skips processing the `NULL` element.