---
layout: default
title: CURRENT_ENGINE
description: Reference material for CURRENT_ENGINE function
grand_parent: SQL functions
parent: Session functions
great_grand_parent: SQL reference
---

# CURRENT_ENGINE

Returns the current engine name.
Returns `system` on the system engine.

## Syntax
{: .no_toc}

```sql
CURRENT_ENGINE()
```

## Return Types
`TEXT`

## Example
{: .no_toc}

```sql
SELECT current_engine()
```

**Returns**: `system`
