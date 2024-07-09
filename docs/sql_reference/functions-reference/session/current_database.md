---
layout: default
title: CURRENT_DATABASE
description: Reference material for CURRENT_DATABASE function
grand_parent: SQL functions
parent: Session functions
great_grand_parent: SQL reference
---

# CURRENT_DATABASE

Returns the current database name; if absent - returns `account_db`

## Syntax
{: .no_toc}

```sql
CURRENT_DATABASE()
```

## Return Types
`TEXT`

## Example
{: .no_toc}

```sql
SELECT current_database()
```

**Returns**: `account_db`