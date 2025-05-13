---
layout: default
title: Organization
description: Use this reference to learn about the metadata available for your Firebolt organization using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for organization

You can use the `information_schema.organization` view to return information about your organization.

You can use a `SELECT` query to return information about your organization, as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.organization;
```

Read more about organizations [here]({% link Overview/organizations-accounts.md %}).

## Columns in information_schema.organization

Each row has the following columns with information about the organization.

| Column Name              | Data Type      | Description                                                                 |
|:-------------------------|:---------------|:----------------------------------------------------------------------------|
| organization_name        | TEXT           | The name of the organization.                                               |
| edition                  | TEXT           | The Firebolt edition used by the organization.                              |
| is_payment_registered    | BOOLEAN        | Specifies if payment is registered for the organization.                    |
| billing_profile_name     | TEXT           | The name of the billing profile for the organization.                       |
| sso                      | TEXT           | JSON configuration for single sign-on (SSO).                                |
| network_policy_name      | TEXT           | The name of the network policy applied at the organization level.           |
| payment_method_name      | TEXT           | The name of the current payment method for the organization.                |
| next_payment_method_name | TEXT           | The name of the next payment method for the organization.                   |
| credits_remaining        | DECIMAL(38, 9) | The remaining credit balance (in US dollars) available to the organization. |
| created                  | TIMESTAMPTZ    | Time (UTC) that the organization was created.                               |
| organization_owner       | TEXT           | The name of the identity that owns this organization.                       |
| last_altered             | TIMESTAMPTZ    | Time (UTC) that the organization was last edited.                           |
| last_altered_by          | TEXT           | Name of the identity that last edited the organization.                     |
