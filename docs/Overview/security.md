---
layout: default
title: Security
description: Introduction to Firebolt security features and functionality
nav_order: 6
parent: Overview
---

# Security
{: .no_toc}

Through a layered security approach to service, Firebolt provides customers with a secure and trusted Cloud Data Warehouse (CDW) for their modern enterprise needs. With advanced security features and industry best practices, Firebolt ensures your data remains secure, compliant, and accessible only to authorized individuals. Access to objects is managed with use of accounts to provide boundaries to isolate and secure data. 

This topic will explore this layered security methodology with 1) network and protocol level security, 2) identity management, 3) access control, and 4) data level protection. 

## Network Security

Firebolt ensures end-to-end encryption using TLS 1.2, safeguarding data transmission from end users to the cloud service. 

In addition to the TLS protocol, Firebolt supports defining custom [network policies](../Guides/security/network-policies.md), add an extra layer of security to an application. This functionality allows administrators fine-grained control over IP ranges that are allowed to access Firebolt. 

{: .note}
Firebolt supports both [login](../Guides/managing-your-organization/managing-logins.md) and [service account](../Guides/managing-your-organization/service-accounts.md) objects - a login object represents a given security principal (human) defined by an email address, while a service account object is used to represent a machine that will authenticate to the system.

In Firebolt, network policies contain allowed_IP_list and blocked_IP_list properties that capture definition of IP address ranges. Each property is a list and can contain one or more IP ranges.

#### Example

```sql
CREATE NETWORK POLICY IF NOT EXISTS my_network_policy WITH ALLOWED_IP_LIST = (‘4.5.6.1’, ‘2.4.5.1’) 
DESCRIPTION = 'my new network policy'
```

Once created, a network policy can be attached to [an organization](../Guides/managing-your-organization/creating-an-organization.md), or to an individual login and/or service account. 

#### Example

```sql
ALTER ORGANIZATION my_organization SET NETWORK_POLICY = my_network_policy;
ALTER LOGIN 'kate@acme.com' SET NETWORK_POLICY = my_network_policy;
```

For more information, see [network policies](../Guides/security/network-policies.md).

## Identity Management

Identity management is a multi-step verification process that is used to ensure that only the right people, services, and applications can get access to organizational resources. Identity management includes user identification and authentication. To strengthen security, many organizations also require [multi-factor authentication (MFA)](../Guides/security/enabling-mfa.md) as an additional  security measure, requiring users to provide two or more forms of identification before authenticating. Firebolt also supports [Single Sign-On (SSO)](../Guides/security/sso/sso.md). SSO simplifies the user authentication process and increases access management security by allowing users to log in to multiple applications and services using a single set of credentials.

Auth0 is used as the identity provider for customer registration, and the authentication data is stored in Auth0 using industry-standard cryptography. Authentication information is exchanged using SAML 2.0 protocol.

### Single Sign-On (SSO)

Firebolt uses SSO to simplify and streamline implementation, enhance security posture, and fortify defenses against unauthorized access and data breach. SSO configuration is accessible to those with the org_account built-in role.

### Multi-Factor Authentication (MFA)

Multi-factor authentication (MFA) adds an extra layer of security by requiring users to provide multiple forms of authentication to access an account. Many industries have specific compliance and regulatory requirements that mandate the use of MFA for certain types of data or systems — Firebolt fully supports these requirements with MFA configuration and implementation that is tied to the login object.

#### Example

```sql
CREATE LOGIN "kate@acme.com" WITH
FIRST_NAME = 'Kate'
LAST_NAME = 'Peterson'
IS_PASSWORD_ENABLED = TRUE
IS_MFA_ENABLED = TRUE;
```

## Access control

Access control ensures that the user has appropriate permissions to engage with the system or resources they attempt to use. At Firebolt, [role-based access control (RBAC)](../Guides/security/rbac.md) mechanisms are implemented for these purposes. In addition to supporting built-in roles, custom or user-defined roles can be created as well. While built-in roles already have a prebuilt set of permissions assigned, permissions can be assigned to user-defined roles (by using GRANT/REVOKE statements).

The RBAC model is centered around the following principles: 
- Any object is  securable.
- Any supported statement is guarded by a permission (allowing no unauthorized actions).
- The RBAC model is composable (effective permissions are the sum of role assignments).
- Roles are hierarchical and can come with inheritance relationships.

The key building blocks/concepts of the Firebolt RBAC model are: [roles](#roles), [users](#users), [objects, and permissions](#objects-and-permissions). 

### Roles 

There are 2 types of roles that exist within Firebolt: 

1) Built-in roles that are available as soon as a new organization and the first account get provisioned.

2) User-defined roles that administrators can create by themselves. 

Creating a role can also be done using the Firebolt UI or [SQL](../sql_reference/commands/access-control/create-role.md).

#### Example

```sql
CREATE ROLE sales;
```
 
A set of [system-defined roles](../Guides/security/rbac.md#system-defined-roles) that align with common user personas and responsibilities are also available. 

### Users

Users are linked to either a login or service account in order to gain access to Firebolt. They can be created using the [CREATE USER](../sql_reference/commands/access-control/create-user.md) statement in SQL or through the Firebolt UI. 

```sql
CREATE USER kate;
CREATE USER bob;
 ```

Roles are assigned to users to allow them to complete tasks on relevant objects to fulfill their business needs.

```sql
GRANT ROLE sales TO kate;    -- grants sales role to user kate
REVOKE ROLE sales FROM bob; -- revokes sales role from user bob 
```

### Objects and Permissions

Permissions define the actions or operations that can be performed within Firebolt. These permissions range from managing databases and engines to executing queries and accessing and analyzing data. Each instance of an object (securable) in the Firebolt object model has specific permissions that are associated with it. As an example, there could be multiple instances of an engine object (i.e. my_engine1, my_engine2) and each instance comes with a set of predefined permissions.

For a full list of available permissions, see [role-based access control](../Guides/security/rbac.md#permissions).

Any permission that Firebolt supports can be granted (or revoked) to (or from) roles. Firebolt supports standard SQL constructs ([GRANT](../sql_reference/commands/access-control/grant.md) and [REVOKE](../sql_reference/commands/access-control/revoke.md)). 

{: .note}
Privileges can only be granted to (and revoked from) roles - roles can then be granted to users to give the access those permissions provide.

#### Example

```sql
GRANT USAGE ON DATABASE sales_db TO sales;    -- grants ability to use sales_db database to sales role
GRANT USAGE ANY DATABASE ON ACCOUNT dev_account TO sales;    -- grants ability to use any database in dev_account account to sales role
REVOKE OPERATE ON ENGINE sales_eng FROM sales;   -- revokes ability to START and STOP engine sales_eng from sales role
```

## Data protection

Firebolt is firmly committed to data security, privacy, and compliance. To deliver on that promise, Firebolt ensures that all data managed by Firebolt is properly safeguarded and protected, enforcing the governance of encryption standards for data in motion and at rest. The following functionality is available for customers automatically out of the box.

### Data at rest
By default, all data is encrypted at rest and stored on Amazon Simple Storage Service (S3) storage. All new objects are encrypted by default with Amazon S3-managed keys or AWS KMS keys stored in AWS Key Management Service. 

### Data in motion
Firebolt automatically encrypts sensitive data that is being transferred/sent within service components, ensuring that as it travels over networks, it's secure and cannot be intercepted by eavesdroppers. 

### Secure communication protocols
Firebolt uses secure communication protocols to add an extra layer of protection against man-in-the-middle attacks.
