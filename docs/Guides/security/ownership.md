---
layout: default
title: Ownership
description: Learn about object Ownership in Firebolt.
parent: Configure security
nav_order: 11
---

# Ownership

Ownership allows users to perform all operations on objects they created without having to manually grant privileges for these operations. This provides a smoother user experience because objects are immediately available to use once created. These operations include granting privileges on owned objects.

## Ownership Levels

Firebolt implements ownership at two distinct levels:

1. **Account-level ownership** &mdash; Applies to objects within an account
2. **Organization-level ownership** &mdash; Applies to objects at the organization level

These two ownership levels are isolated from each other&mdash; you cannot make a user the owner of an organization-level object, and you cannot make a login or service account the owner of an account-level object.

## Supported Object Types

### Account-Level Objects

The account-level object types that support ownership are:
- Role
- User
- Engine
- Database
- Schema
- Table
- View

### Organization-Level Objects

The organization-level object types that support ownership are:
- Organization
- Account
- Login
- Service Account
- Network Policy

## Viewing Current Owners

The current owner of an object can be viewed in the corresponding information_schema view:

### Account-Level Objects

| Object   | View                                                                     |
|:---------|:-------------------------------------------------------------------------|
| Role     | N/A                                                                      |
| User     | [information_schema.users][users]                                        |
| Database | [information_schema.catalogs][catalogs]                                  |
| Engine   | [information_schema.engines][engines]                                    |
| Schema   | [information_schema.schemata][schemata]                                  |
| Table    | [information_schema.tables][tables]                                      |
| View     | [information_schema.views][views] or [information_schema.tables][tables] |

{: .note}
Index ownership, shown in [information_schema.indexes][indexes], will always show the table owner as an index's owner.

### Organization-Level Objects

| Object          | View                                                    |
|:----------------|:--------------------------------------------------------|
| Organization    | [information_schema.organization][organization]         |
| Account         | [information_schema.accounts][accounts]                 |
| Login           | [information_schema.logins][logins]                     |
| Service Account | [information_schema.service_accounts][service_accounts] |
| Network Policy  | [information_schema.network_policies][network_policies] |

## Changing an Object's Owner

### Account-Level Objects

The owner of an account-level object may alter its ownership using the following syntax:
```sql
ALTER <object type> <object name> OWNER TO <user>
```

Examples:
```sql
ALTER DATABASE db OWNER TO new_owner
ALTER ENGINE eng OWNER TO new_owner
ALTER ROLE r OWNER TO new_owner
ALTER USER u OWNER TO new_owner
ALTER SCHEMA public OWNER TO new_owner
ALTER TABLE t OWNER TO new_owner
ALTER VIEW v OWNER TO new_owner
```

### Organization-Level Objects

The owner of an organization-level object may alter its ownership using the following syntax:
```sql
ALTER <object type> <object name> OWNER TO <identity>
```

Where `<identity>` refers to a login or service account.

Examples:
```sql
ALTER ORGANIZATION my_organization OWNER TO "alice@acme.com"
ALTER ACCOUNT dev OWNER TO "alice@acme.com"
ALTER LOGIN "bob@acme.com" OWNER TO "alice@acme.com"
ALTER SERVICE ACCOUNT "machine_user" OWNER TO "alice@acme.com"
ALTER NETWORK POLICY "my_policy" OWNER TO "alice@acme.com"
```

## Dropping Objects with Ownership Relationships

### Dropping Users that Own Objects

Any objects owned by a user must first be dropped or have their owner changed before dropping the user.

{: .note}
A table owner can drop the table even if there are views referencing it that are not owned by the table's owner, using the `CASCADE` parameter to [DROP TABLE]({% link sql_reference/commands/data-definition/drop-table.md %}).

### Dropping Logins or Service Accounts that Own Objects

Similarly, any organization-level objects owned by a login or service account must first be dropped or have their owner changed before dropping the login or service account.

## Managing Ownership in the Firebolt Workspace

You can use the user interface in the **Firebolt Workspace** to transfer ownership of objects as follows:

1. Log in to the [Firebolt Workspace](https://firebolt.go.firebolt.io/signup). If you don't yet have an account with Firebolt, you can sign up for one.
2. Select the Govern icon (<img src="../../assets/images/govern-icon.png" alt="The icon to open the Govern Space." width="20"/>) in the left navigation pane to open the **Govern Space**.
3. Select **Ownership** from the left navigation pane.
4. Select the three horizontal dots (...) to the right of the object that you want to transfer ownership of.
5. Select **Transfer ownership** from the drop-down list.
6. In the **Transfer ownership** window that opens, choose a new owner from the drop-down list.
7. Select the **Transfer ownership** button to confirm.

### Viewing all Objects Owned by a User

1. From the [Firebolt Workspace](https://firebolt.go.firebolt.io/signup), select the Govern icon (<img src="../../assets/images/govern-icon.png" alt="The icon to open the Govern Space." width="20"/>) in the left navigation pane to open the **Govern Space**.
2. Select **Users** from the left navigation pane.
3. Select the user from the **User Name** column.
4. Select the **Ownership** tab to view a list of objects owned by the selected user.

### Bulk Transferring or Deleting Objects Owned by a User

1. From the [Firebolt Workspace](https://firebolt.go.firebolt.io/signup), select the Govern icon (<img src="../../assets/images/govern-icon.png" alt="The icon to open the Govern Space." width="20"/>) in the left navigation pane to open the **Govern Space**.
2. Select **Users** from the left navigation pane.
3. Select the three horizontal dots (...) to the right of the user whose objects you want to transfer ownership of.
4. Select **Transfer ownership** from the drop-down list.
5. In the window that opens, select the checkboxes next to objects that you want to delete or transfer ownership of.
6. Select the **Delete object** or **Transfer ownership** button to apply changes.

{: .note}
Ownership transfer using the **Firebolt Workspace** is not available for `Schema`, `Table`, and `View` objects. These must be modified using SQL commands in the **Develop Workspace** or using the [Firebolt API]({% link API-reference/index.md %}).

{: .note}
The Firebolt Workspace currently only supports managing ownership for account-level objects. Organization-level object ownership must be managed using SQL commands.

[users]: {% link sql_reference/information-schema/users.md %}
[catalogs]: {% link sql_reference/information-schema/catalogs.md %}
[engines]: {% link sql_reference/information-schema/engines.md %}
[schemata]: {% link sql_reference/information-schema/schemata.md %}
[tables]: {% link sql_reference/information-schema/tables.md %}
[views]: {% link sql_reference/information-schema/views.md %}
[indexes]: {% link sql_reference/information-schema/indexes.md %}
[organization]: {% link sql_reference/information-schema/organization.md %}
[accounts]: {% link sql_reference/information-schema/accounts.md %}
[logins]: {% link sql_reference/information-schema/logins.md %}
[service_accounts]: {% link sql_reference/information-schema/service-accounts.md %}
[network_policies]: {% link sql_reference/information-schema/network_policies.md %}
