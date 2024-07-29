---
layout: default
title: SQL functions
description: Reference for SQL functions available in Firebolt.
parent: SQL reference
has_children: true
has_toc: false
---

# SQL functions

See a [full function glossary](./functions-glossary.md), or find functions based on type from the list below. 

* [Aggregation functions](./aggregation/index.md)  
  Perform a calculation across a set of rows, returning a single value. 

* [Array functions](./array/index.md)  
  Used for the manipulation and querying of `ARRAY`-type data, such as transforming and filtering. Includes [Lambda functions](./Lambda/index.md). 

* [Binary functions](./bytea/index.md)
  Used for manipulation and querying of `BYTEA`-type data, such as encoding and decoding. 

* [Conditional and miscellaneous functions](./conditional-and-miscellaneous/index.md)  
  Include various methods for modifying data types and applying conditional operations.  

* [DataSketches functions](./datasketches/index.md)
  Apache Datasketches is a library designed to efficiently summarize and analyze large-scale data using probabilistic data structures known as sketches. These sketches provide approximate answers to complex queries, such as distinct counting, quantile estimation, and frequency estimation, with high accuracy and significantly reduced memory usage. This makes Datasketches ideal for big data applications where traditional exact methods are impractical due to time or space constraints.

* [Date and time functions](./date-and-time/index.md)  
  Manipulate date and time data types.

* [JSON functions](./JSON/index.md)  
  Extract and transform JSON into Firebolt native types, or JSON sub-objects. Used either during the ELT process or applied to columns storing JSON objects as plain `TEXT`

* [Numerical functions](./numeric/index.md)  
  Manipulate data types including `INTEGER`, `BIGINT`, `DOUBLE PRECISION`, and other numeric types

* [String functions](./string/index.md)  
  Manipulate string data types

* [Window functions](./window/index.md)  
  Perform a calculation across a specified set of table rows