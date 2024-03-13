---
layout: default
title: ILIKE
description: Reference material for ILIKE function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# ILIKE

Allows matching of strings based on comparison to a pattern. `ILIKE` is normally used as part of a `WHERE` clause. `ILIKE` is case-insensitive; use [LIKE](like.md) for case-sensitive pattern matching. Note that Firebolt uses the `ucs_basic` collation (see below).

## Syntax
{: .no_toc}

```sql
<expression> ILIKE '<pattern>'
```

## Parameters
{: .no_toc}

| Parameter | Description |Supported input types |
| :-------- | :---------- | :---------------------|
| `<expression>` | Any expression that evaluates to `TEXT` | `TEXT` |
| `<pattern>` | Specifies the pattern to match (case-insensitive). | `TEXT` constant. SQL wildcards are supported: <br> <br>* Use an underscore (`_`) to match any single character<br>* Use a percent sign (`%`) to match any number of any characters, including no characters. |


## Return Type
`BOOLEAN`

## Example

Find nicknames from the `players` table that partially match the string "Joe" and any following characters as follows:

```sql
SELECT
	playerid, nickname, email
FROM
	players
WHERE
	nickname ILIKE 'Joe%';
```

**Returns**:

| playerid | nickname | email                   |
|:---------|:----------|:-----------------------|
| 160      | joedavis | cgarcia@example.org     |
| 519 	   | joe79    | jennifer10@example.net  |
| 3692 	   | joeli    | cperez@example.net      |
| 3891	   | joel11   | joanncain@example.net   |
| 4233 	   | joellong | millerholly@example.net |
| 4627 	   | joebowen | amandalewis@example.net |

## Unicode Behavior

Firebolt uses the `ucs_basic` collation, therefore `ILIKE` case insensitivity is limited to ASCII characters. Non-ASCII upper- and lower-case characters are not taken into account:
```sql
SELECT 'ENCYCLOPÆDIA' ILIKE 'encyclopædia'; -- returns false
SELECT 'ENCYCLOPÆDIA' ILIKE 'encyclopÆdia'; -- returns true
SELECT 'MÜNCHEN' ILIKE 'München'; -- returns false
SELECT 'MÜNCHEN' ILIKE 'mÜnchen'; -- returns true
```
