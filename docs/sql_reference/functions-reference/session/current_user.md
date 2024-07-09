---
layout: default
title: CURRENT_USER
description: Reference material for CURRENT_USER function
grand_parent: SQL functions
parent: Session functions
great_grand_parent: SQL reference
---
# CURRENT_USER

Returns the current user name. 

## Syntax
{: .no_toc}

```sql
CURRENT_USER()
```

## Return Types
`TEXT`

## Example
{: .no_toc}
```sql
SELECT current_user()
```

**Returns**: `admin_user`


To return all of the effective privileges of the current user:

```sql
SELECT
  AR.grantee,
  AR.role_name,
  OP.privilege_type,
  OP.object_type,
  OP.object_name
FROM information_schema.transitive_applicable_roles AS AR
JOIN information_schema.object_privileges AS OP
ON (AR.role_name = OP.grantee)
WHERE
  AR.grantee = current_user();
```

**Returns**: 
| grantee | role_name | privilege_type | object_type | object_name |
|:----------|:--------------|-------|----------|----------|
| test_user | account_admin | USAGE | engine | engine1 | 
| test_user | account_admin | USAGE | database | db1 |