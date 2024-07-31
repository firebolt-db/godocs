---
layout: default
title: ALTER SCHEMA
description: Reference and syntax for the ALTER SCHEMA command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# ALTER SCHEMA

Updates the specified SCHEMA.

## ALTER SCHEMA OWNER TO

Change the owner of a schema.<br>The current owner of a view can be viewed in the `information_schema.schemata` view on `schema_owner` column.

check [ownership](../../../Guides/security/ownership.md) page for more info.

### Syntax

```sql
ALTER SCHEMA <schema> OWNER TO <user>
```

### Parameters 
{: .no_toc}

| Parameter | Description |
| :--- | :--- |
| `<schema>` | Name of the schema to change the owner of. |
| `<user>` | The new owner of the view. |