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

## DB version 3.33
**April 2024**

* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### Enhancements, changes and new integrations

<!--- FIR-32055 --->**Removed 'element_at' Function**

The `element_at` function for arrays has been removed and replaced with the `[]` operator. 

<!--- FIR-31458 --->**Change of return type from BIGINT to INTEGER**

The `index_of`/`array_position` function now returns INTEGER instead of BIGINT. 

<!--- FIR-31280 --->**Removed LIMIT DISTINCT syntax**

The `LIMIT_DISTINCT` syntax is no longer supported by Firebolt. 

### Resolved issues

<!--- FIR-31069 --->
* Fixed a bug in `array_position` where searching for `NULL` in an array with non-null elements incorrectly returned a match in some cases. 