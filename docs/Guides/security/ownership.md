---
layout: default
title: Ownership
description: Learn about object Ownership in Firebolt.
parent: Configure security
nav_order: 11
grand_parent: Guides
---

# Ownership

Ownership allows users to perform operations on any object they create without having to be granted the required priviliges. This allows for a smoother user experience, as objects are immediately avaialble to use as they are created.

## Objects that support ownership

The objects that support ownership are:
- Role
- User
- Database
- Engine
- Schema
- Table
- View

The current owner of an object can be viewed in the corresponding information_schema view:
|Object|View|
|:-|:-|
| Role | N/A |
| User | [information_schema.users](../../sql_reference/information-schema/users.md) |
| Database | information_schema.catalogs |
| Engine | [information_schema.engines](../../sql_reference/information-schema/engines.md) |
| Schema | information_schema.schemata |
| Table | [information_schema.tables](../../sql_reference/information-schema/tables.md) |
| View | [information_schema.views](../../sql_reference/information-schema/views.md) or [information_schema.tables](../../sql_reference/information-schema/tables.md) |

{: .note}
Index ownership, shown in [information_schema.indexes](../../sql_reference/information-schema/indexes.md), will always show the table owner as an index's owner.

## Changing an object's owner

The owner of an object may alter its ownership using the following syntax:
```
ALTER <object type>  <object name> OWNER TO <user>
```
Examples:
```
ALTER DATABASE db OWNER TO new_owner
ALTER ENGINE eng OWNER TO new_owner
ALTER ROLE r OWNER TO new_owner
ALTER USER u OWNER TO new_owner
ALTER SCHEMA public OWNER TO new_owner
ALTER TABLE t OWNER TO new_owner
ALTER VIEW v OWNER TO new_owner
```

## Dropping users that own objects

Any objects owned by a user must first be dropped or have their owner changed before dropping the user.