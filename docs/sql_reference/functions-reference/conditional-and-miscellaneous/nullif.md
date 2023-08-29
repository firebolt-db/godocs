---
layout: default
title: NULLIF
description: Reference material for NULLIF function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# NULLIF

Compares two expressions. Returns `NULL` if the expressions evaluate to equal values. Returns the result of `<expression1>` if they are not equal. To return `<expression2>` instead, use `IFNULL`.

## Syntax
{: .no_toc}

```sql
NULLIF(<expression1>, <expression2>)
```

## Parameters 
{: .no_toc}

| Parameter | Description | Supported input types | 
| :-------- | :---------- |:---------|
| `<expression1>`, `<expression2>` | Expressions that evaluate to any data type that Firebolt supports | Any | 

## Return Types 
Returns `NULL` if expressions are equal. Returns `<expression1>` if values are not equal. 


## Example
{: .no_toc}
This example below highlights an instance where `NULL` would be returned: 

```sql
NULLIF('Level 3','Level 3')
```

**Returns**: `NULL`

This example returns `<expression1>` because the values are not equal: 

```sql
NULLIF('Level4','level 4')
```

**Returns**: `Level4`
