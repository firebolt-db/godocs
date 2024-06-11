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

* [Breaking Changes](#breaking-changes)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)

### Breaking Changes 
{: style="color:red;"}

<!--- FIR-33028 --->**Array Casting Nullability Update**
{: style="color:red;"}

Cast to array will no longer support specifying nullability of the inner type. 
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

<!--- FIR-32252 --->**Postgres-compliant Cast**
{: style="color:red;"}

Casts now behave the same across the product and adhere to the list of supported casts. Some usages of casts (explicit, implicit, or assignment cast) that were previously allowed are no longer supported and now result in errors. For more details, see the documentation [here](https://docs.firebolt.io/godocs/sql_reference/data-types.html#type-conversion).

### Enhancements, changes and new integrations
{: style="color:black;"}

<!--- FIR-32711 --->**Query Cancelation on HTTP Connection Drop**

Going forward, when the network connection between the client and Firebolt is dropped (for example because the Firebolt UI tab was closed or due to network issues), DML queries (INSERT, UPDATE, DELETE, etc) are no longer canceled automatically, but will keep running in the background. You can continue to monitor their progress in `information_schema.engine_running_queries` or cancel them manually using the `cancel query` statement if desired. DQL queries (SELECT) are still canceled automatically on connection drop. 

<!--- FIR-31795 --->**New Aggregate Functions: `CHECKSUM` and `hash_agg`**

`CHECKSUM` and `hash_agg` functions are now supported for aggregating indexes. Note that when the `hash_agg` function doesn't receive rows, the result is 0.