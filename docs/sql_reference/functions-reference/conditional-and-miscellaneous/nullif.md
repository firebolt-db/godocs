---
layout: default
title: NULLIF
description: Reference material for NULLIF function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
---

# NULLIF

The `NULLIF` function compares the values of its parameters and returns `NULL` if they are equal. Otherwise, it returns the value of its first parameter. 
Therefore, `NULLIF` performs the inverse operation of the [COALESCE](./coalesce.md) function.

## Syntax
{: .no_toc}

```sql
NULLIF(<expression1>, <expression2>)
```

## Parameters 
{: .no_toc}

| Parameter | Description |Supported input types | 
| :-------- | :---------- |:---------|
| `<expression1>` | Expression of any type that is comparable to the type of `<expression2>` | Any | 
| `<expression2>` | Expression of any type that is comparable to the type of `<expression1>` | Any | 

If `<expression1>` and `<expression2>` have different types, they will be promoted to their least common supertype for the purpose of comparison. The same type promotion rules as for the regular comparison operators (e.g. `=`) apply.

## Return Types 

If `<expression1>` and `<expression2>` have the same type, this will also be the return type of the `NULLIF` function. 
If `<expression1>` and `<expression2>` have different types, the return type will be the least common supertype to which they are promoted for comparison purposes. 

## Example
{: .no_toc}

This example below highlights an instance where `NULL` would be returned from `NULLIF`: 

```sql
NULLIF('(none)', '(none)')
```

**Returns**: The `TEXT` value `NULL`

In the next example, `NULLIF` returns the value of `<expression1>` because it is not equal to the value of `<expression2>`: 

```sql
NULLIF('Level 4', '(none)')
```

**Returns**: The `TEXT` value `'Level 4'`

Finally, the following example illustrates type promotion if the parameters to `NULLIF` have different types:

```sql
NULLIF(3.14::REAL, 42::BIGINT)
```

**Returns**: The `DOUBLE` value `3.14`, since the least common supertype of `REAL` and `BIGINT` is `DOUBLE`.
