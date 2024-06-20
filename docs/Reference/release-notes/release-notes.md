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

## DB version 4.1
**June 2024**

* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### Enhancements, changes and new integrations
{: style="color:black;"}

<!--- FIR-32411 --->**Removing `connect` and `modify account` Privileges**

Removed `connect` and `modify account` privileges from object_privileges and the code base to reduce confusion. They will no longer appear for new accounts. 

### Resolved issues

<!--- FIR-32985--->
* Fixed an issue causing errors when using `WHERE column IN (...)` filters on external table scans.





