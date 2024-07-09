---
layout: default
title: ALTER ROLE
description: Reference and syntax for the ALTER ROLE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# ALTER ROLE

Updates the specified role.

## ALTER ROLE OWNER TO

Change the owner of a role.

### Syntax

```sql
ALTER ROLE <role> OWNER TO <user>
```

### Parameters 
{: .no_toc}

| Parameter | Description |
| :--- | :--- |
| `<role>` | Name of the role to change the owner of. |
| `<user>` | The new owner of the role. |
```
