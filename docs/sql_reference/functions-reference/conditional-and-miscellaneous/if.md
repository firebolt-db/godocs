---
layout: default
title: IF
description: Reference material for IF function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
---

# IF

Evaluates a condition and returns different results based on whether the condition is true or false. The `IF` function is a simplified alternative to the `CASE` expression for handling conditional logic. 


## Syntax
{: .no_toc}

```sql
IF(<condition>, <then>, <else>)
```

## Parameters 
{: .no_toc}

| Parameter     | Description      | Supported input types | 
| :------------- | :-------------------------- | :--------|
| `<condition>` | Condition that the function evaluates.  |  `BOOLEAN` | 

| `<then>`    | Value returned when <condition> evaluates to `true`. | Any |

| `<else>`    | Value returned when <condition> evaluates to `false` or `NULL`. Must match the data type of <then>. | Any |


## Return type 
The `IF` function returns the same data type as the <then> and <else> parameters. 


## Example
{: .no_toc}
The following example uses the `IF` function to determine if the current day is a weekend or weekday:
```sql
SELECT IF(EXTRACT(DOW FROM CURRENT_DATE()) % 6 = 0, 'Weekend', 'Weekday')
```

The previous query returns:
* `Weekend` when the current day is Saturday or Sunday. 
* `Weekday` for any other day. 

