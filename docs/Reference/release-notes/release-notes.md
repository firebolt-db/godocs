---
layout: default
title: Release notes
description: Latest release notes for the Firebolt data warehouse.
parent: General reference
nav_order: 1
has_toc: false
has_children: false
---

# Release notes

Firebolt continuously releases updates so that you can benefit from the latest and most stable service. These updates might happen daily, but we aggregate release notes to cover a longer time period for easier reference. The most recent release notes from the latest version are below. 

- See the [Release notes archive](../release-notes/release-notes-archive.md) for earlier-version release notes.

{: .note}
Firebolt might roll out releases in phases. New features and changes may not yet be available to all accounts on the release date shown.

## DB version 4.0
**June 2024**

* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)

### Enhancements, changes and new integrations

<!--- FIR-33028 --->**Array Casting Nullability Update**

Cast to array will no longer support writing nullability of the compound type. 
Example: 

```sql
a::array(int null)
``` 
or 
```sql
cast(a as array(int not null)) 
```
will now fail, and need to be rewritten as: 
```sql
a::array(int) 
``` 
or 
```sql
cast(a as array(int)). 
```

<!--- FIR-32711 --->**Query Cancelation on HTTP Connection Drop**

DML queries will be canceled on HTTP connection drop, such as `SELECT`. Note that `INSERT` queries will not be canceled. 

<!--- FIR-31795 --->**New Aggregate Functions: `CHECKSUM` and `hash_agg`**

`CHECKSUM` and `hash_agg` functions are now supported for aggregating indexes. Note that when the `hash_agg` function doesn't receive rows, the result is 0.