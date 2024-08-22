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

## Example 1
{: .no_toc}
```sql
-- executed by user bob
SELECT session_user()
```

**Returns**: `bob`

## Example 2
Shows effective privileges of the roles directly assigned to the user running the query:

```sql
SELECT
AR.grantee,
  AR.role_name,
  OP.privilege_type,
  OP.object_type,
  OP.object_name
FROM information_schema.applicable_roles AS AR
JOIN information_schema.object_privileges AS OP
ON (AR.role_name = OP.grantee)
WHERE
  AR.grantee = session_user();
```

**Returns**: 

| grantee   | role_name     | privilege_type | object_type | object_name |
|:----------|:--------------|:---------------|:------------|:------------|
| test_user | account_admin | USAGE | engine | engine1 | 
| test_user | account_admin | USAGE | database | db1 |

## Example 3

Dynamic security through view which uses session_user().

```sql
-- user bob created view:
create view my_employee_data as select * from employees where user_name = session_user();

-- user alice queries it:
select * from my_employee_data; -- session_user() will be evaluated to 'alice' for this query
```

**Returns**: 

| user_name   | ...   | 
|:------------|:-------------------|
| alice |... | 
