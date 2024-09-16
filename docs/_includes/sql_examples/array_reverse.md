{% raw %}
The following example returns the reverse of the input array:
``` sql
SELECT ARRAY_REVERSE([1, 2, NULL, 3, 6]) as res;
```

| res (ARRAY(INTEGER)) |
| :--- |
| {6,3,NULL,2,1} |
{% endraw %}

{% raw %}
Only the outermost array is reversed for nested arrays:
``` sql
SELECT ARRAY_REVERSE([[1,2,3], [4,5], NULL, [7], [8,9]]) as res;
```

| res (ARRAY(ARRAY(INTEGER))) |
| :--- |
| {{8,9},{7},NULL,{4,5},{1,2,3}} |
{% endraw %}