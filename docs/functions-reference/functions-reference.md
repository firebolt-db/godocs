---
layout: default
title: SQL Functions
description: Reference for SQL functions available in Firebolt.
nav_order: 15
has_children: true
has_toc: false
---

# SQL functions

* [Aggregate array functions](./aggregate-array/index.md)  
  These functions work on array-typed columns, but instead of being applied row by row, they combine the results of all the arrays belonging to each of the groups defined by the `GROUP BY` clause.

* [Aggregation functions](./aggregation/index.md)  
  These functions perform a calculation across a set of rows, returning a single value.

* [Array functions](./array/index.md)  
  Used for the manipulation and querying of `ARRAY`-type data, such as transforming and filtering. Includes [Lambda functions](./Lambda/index.md).

* [Binary functions](./bytea/index.md)  
  Used for manipulation and querying of `BYTEA`-type data, such as encoding and decoding. 

* [Conditional and miscellaneous functions](./conditional-and-miscellaneous/index.md)  
  These functions include various methods for modifying data types and applying conditional operations.   

* [Date and time functions](./date-and-time/index.md)  
  Functions for manipulating date and time data types.   

* [JSON functions](./JSON/index.md)  
  These functions extract and transform JSON into Firebolt native types, or JSON sub-objects. They are used either during the ELT process or applied to columns storing JSON objects as plain `TEXT`.

* [Numeric functions](./numeric/index.md)  
  Functions for manipulating data types including `INTEGER`, `BIGINT`, `DOUBLE PRECISION`, and other numeric types.

* [String functions](./string/index.md)  
  Functions for manipulating string data types

* [Window functions](./window/index.md)  
  These functions perform a calculation across a specified set of table rows.









