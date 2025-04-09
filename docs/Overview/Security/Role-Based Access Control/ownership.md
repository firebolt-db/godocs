---
redirect_from:
  - /Overview/Role-Based Access Control/ownership.html
layout: default
title: Ownership
description: Learn about ownership in Firebolt & how it impacts permissions and access control.
parent: Role-Based Access Control
nav_order: 7
---

# Ownership

When you create an object in Firebolt, you become its owner. As the owner, you have full control and can perform all operations on the object without needing additional privileges. This allows you to use objects immediately after creating them.

As the owner of an object, you can do the following:
* Grant privileges on the object to any role.
* Grant roles you own to other users or roles without needing administrator permissions.
* Transfer ownership of the object to another entity.

## Supported object types

Firebolt supports ownership at both the organization level and the account level.

### Organization-level objects

The following organization-level objects support ownership:

* **Organization**
* **Account**
* **Login**
* **Service account**
* **Network policy**

Organization-level object owners must be either a login or a service account. You cannot make a user the owner of an organization-level object.

### Account-level objects

The following account-level objects support ownership:

* **Role**
* **User**
* **Engine**
* **Database**
* **Schema**
* **Table**
* **View**

Account-level object owners must be users. You cannot make a login or service account the owner of an account-level object.

## Viewing object ownership

The current owner of an object can be viewed in the corresponding `information_schema` view:

| Object Type     | View                                                      |
|-----------------|-----------------------------------------------------------|
| Organization    | `information_schema.organization`                         |
| Account         | `information_schema.accounts`                             |
| Login           | `information_schema.logins`                               |
| Service Account | `information_schema.service_accounts`                     |
| Network Policy  | `information_schema.network_policies`                     |
| Role            | N/A                                                       |
| User            | `information_schema.users`                                |
| Database        | `information_schema.catalogs`                             | 
| Engine          | `information_schema.engines`                              |
| Schema          | `information_schema.schemata`                             |
| Table           | `information_schema.tables`                               |
| View            | `information_schema.views` or `information_schema.tables` |

{: .note}
Indexes inherit ownership from their parent table. In `information_schema.indexes`, the table owner is displayed as the index owner.

## Changing an object's owner

You can transfer ownership of an object using the following syntax:

```sql
ALTER <object type> <object name> OWNER TO <identity>
```

Note that the identity type must match the level of the object:
- For organization-level objects, you must specify a login or service account.
- For account-level objects, you must specify a user.

## Examples of updating ownership permissions

The following examples demonstrate how to change the ownership of different object types.

### Organization-level objects

```sql
ALTER ORGANIZATION my_organization OWNER TO "alice@acme.com"
ALTER ACCOUNT dev OWNER TO "alice@acme.com"
ALTER LOGIN "bob@acme.com" OWNER TO "alice@acme.com"
ALTER SERVICE ACCOUNT "machine_user" OWNER TO "alice@acme.com"
ALTER NETWORK POLICY "my_policy" OWNER TO "alice@acme.com"
```

### Account-level objects

```sql
ALTER DATABASE db OWNER TO new_owner
ALTER ENGINE eng OWNER TO new_owner
ALTER ROLE r OWNER TO new_owner
ALTER USER u OWNER TO new_owner
ALTER SCHEMA public OWNER TO new_owner
ALTER TABLE t OWNER TO new_owner
ALTER VIEW v OWNER TO new_owner
```

### Dropping users that own objects

Before dropping a user who owns objects, you must either drop the objects owned by the owner or transfer ownership of them to another user.

The following code example shows how to drop a table that has dependent views not owned by the table's owner using the `CASCADE` parameter to enforce the drop:

```sql
DROP TABLE <table_name> CASCADE;
```