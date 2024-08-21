---
layout: default
title: CURRENT_ENGINE
description: Reference material for CURRENT_ENGINE function
parent: Session functions
---

# CURRENT_ENGINE

Returns the current engine name.
Returns `system` on the [system engine](../../../Guides/operate-engines/system-engine.md).

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