---
layout: default
title: Aggregate array functions
description: Reference for aggregate array functions
nav_order: 1
parent: SQL functions
grand_parent: SQL reference
has_children: false
published: false
---

## Aggregate array functions

Aggregate semi-structured functions work globally on all the arrays in a given column expression, instead of a row-by-row application.

At their simplest form (without a `GROUP BY` clause) - they will provide the result of globally applying the function on all of the elements of the arrays in the column expression specified as their argument. For example, `ARRAY_SUM_GLOBAL` will return the sum of all the elements in all the array of the given column. `ARRAY_MAX_GLOBAL` will return the maximum element among all of the elements in _all_ of the arrays in the given column expression.

When combined with a `GROUP BY` clause, these operations will be performed on all of the arrays in each group.
