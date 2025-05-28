---
layout: default
title: ICU_NORMALIZE
description: Reference material for ICU_NORMALIZE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
---

# ICU_NORMALIZE
Transliterate a string using a specified ICU transliterate ID.

## Syntax
{: .no_toc}

```sql
ICU_NORMALIZE(<expression>, <transliterate_id>)
```

## Parameters
{: .no_toc}

| Parameter            | Description                                                              | Supported input types |
|:---------------------|:-------------------------------------------------------------------------|:----------------------|
| `<expression>`       | An input string to transliterate.                                        | `TEXT`                |
| `<transliterate_id>` | A valid [ICU library](https://icu.unicode.org/) transliterate ID string. | `TEXT`                |

## Return Type

The `ICU_NORMALIZE` function returns a result of type `TEXT`.

## Errors

If `<transliterate_id>` is invalid, an error is thrown.

## Examples
{: .no_toc}

<!--Revive and remove later code once 4.23 is rolled: {% include sql_examples/icu_normalize_executable.md %}-->
{% include sql_examples/icu_normalize.md %}