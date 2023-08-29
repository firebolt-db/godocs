---
layout: default
title: CITY_HASH
description: Reference material for CITY_HASH function
nav_exclude: true
search_exclude: true
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# CITY_HASH

Takes one or more input parameters of any data type and returns a 64-bit non-cryptographic hash value. `CITY_HASH` uses the CityHash algorithm for string data types, implementation-specific algorithms for other data types, and the CityHash combinator to produce the resulting hash value.

## Syntax
{: .no_toc}

```sql
CITY_HASH(<expression>, [, expressionn [,...]])
```
## Parameters 
{: .no_toc}

| Parameter | Description                          |Supported input types | 
| :--------- | :---------------------------------- | :----------|
| `<expression>`   | An expression that returns any data type that Firebolt supports. | Any | 

## Return type
`BIGINT`

## Example
{: .no_toc}

The following examples returns a hash value from three parameters relating to a particular video game player, including their username and registration date: 

```sql
SELECT CITY_HASH('esimpson', '08-25-2016')
```

**Returns:** `-6,509,667,128,195,191,394`
