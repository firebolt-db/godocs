---
layout: default
title: SESSION_USER
description: Reference material for SESSION_USER function
grand_parent: SQL functions
parent: Session functions
great_grand_parent: SQL reference
---
# SESSION_USER

Returns the name of the user running the current query.

## Syntax
{: .no_toc}

```sql
SESSION_USER()
```

## Return Types
`TEXT`

## Examples
{: .no_toc}

{% include sql_examples/current_user_executable.md %}

**Example**

Dynamic security through a view which uses `session_user()`.

```sql
-- user bob created view:
create view my_employee_data as select * from employees where user_name = session_user();

-- user alice queries it:
select * from my_employee_data; -- session_user() will be evaluated to 'alice' for this query
```

**Returns** 

| user_name   | ...   | 
|:------------|:-------------------|
| alice |... | 
