---
layout: default
title: URL_ENCODE
description: Reference material for URL_ENCODE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
published: true
---

# URL\_ENCODE

Encodes all characters that are not unreserved using [percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding).

Unreserved characters are defined according to [W3C RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html).

```
unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"
```

## Syntax
{: .no_toc}

```sql
URL_ENCODE(<expression>)
```

## Parameters
{: .no_toc}

| Parameter | Description                |Supported input types |
| :--------- | :------------------------ | :--------------------|
| `<expression>` | The string to be encoded. | `TEXT` |

## Return Type
{: .no_toc}

`TEXT`

## Example
{: .no_toc}

The example below converts characters that are not unreserved that appear in the parameter section of the URL:

```sql
SELECT CONCAT('https://www.firebolt.io/?', URL_ENCODE('example_id=1&hl=en'));
```

**Returns**: https://www.firebolt.io/?example_id%3D1%26hl%3Den

## Related

* [URL_DECODE](url_decode.md)
