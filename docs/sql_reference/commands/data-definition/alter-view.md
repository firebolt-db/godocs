---
layout: default
title: ALTER VIEW
description: Reference and syntax for the ALTER VIEW command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# ALTER VIEW

Updates the specified VIEW.

## ALTER VIEW OWNER TO

Change the owner of a view. The current owner of a view can be viewed in the `information_schema.views` view on `view_owner` column.

check [ownership](../../../Guides/security/ownership.md) page for more info.

### Syntax

```sql
ALTER VIEW <view> OWNER TO <user>
```

### Parameters 
{: .no_toc}

| Parameter | Description |
| :--- | :--- |
| `<view>` | Name of the view to change the owner of. |
| `<user>` | The new owner of the view. |