---
layout: default
title: NGRAM
description: Reference material for NGRAM function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
published: true
---

# NGRAM

This function takes an integer `n` and a text sequence, then splits the sequence into
overlapping contiguous subsequences of length `n`.


## Syntax

{: .no_toc}

```sql
NGRAM( <n>, <text> )
```

## Parameters

{: .no_toc}

| Parameter | Description                                      | Datatype  |
|:----------|:-------------------------------------------------|:----------|
| `<n>`     | An integer specifying the length of each n-gram. | `INTEGER` |
| `<text>`  | The text sequence to split into n-grams.         | `TEXT`    |

## Return Types

`ARRAY(TEXT)`

- If any of the inputs is nullable, the result type is `ARRAY(TEXT) NULL`.

## Behavior

The function splits the input text into overlapping contiguous subsequences of length `n`.
- If `n` is smaller than the size of the input text, an array containing the single value of the input text is returned.
- If `n` is smaller than 1, an error is thrown.
- If any input is `NULL`, the result is `NULL` regardless of the other input value.

## Errors

An error is thrown if `n` is smaller than 1.

## Respect/Ignore Nulls

Propagates nulls: If any input is `NULL`, the result is `NULL`.

## Examples

{: .no_toc}

{% include sql_examples/ngram.md %}
