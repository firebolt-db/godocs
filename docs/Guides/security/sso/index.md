---
redirect_from:
  - /Guides/security/sso/sso.html
  - /Guides/security/sso/configuring-idp-for-sso.html
layout: default
title: Configure SSO
description: Learn about how to set up SSO authentication for Firebolt.
nav_order: 2
parent: Configure security
grand_parent: Guides
has_toc: false 
has_children: true
---

# Configure your IdP

An **Identity Provider (IdP)** is a service that handles user authentication and manages user identities. When you set up Single Sign-On (SSO), the IdP verifies your users' credentials and allows them to access multiple applications, including Firebolt, without needing to login repeatedly.  

For your organization, an IdP simplifies user management and strengthens security. You can enforce centralized security policies, like multi-factor authentication (MFA), and quickly revoke access when someone leaves the team. 

For your users, using single sign-on gives them access to all the tools they need, including Firebolt.


Single-sign on (SSO) is an authentication process that allows access to multiple applications or services with a single set of credentials. It provides a centralized authentication mechanism for your organization so that it's easier to manage user access, enforce security policies, and revoke access when necessary.

## Pre-requisites

Before you can use SSO with Firebolt, you must complete specific configuration steps in your Identity Provider (IdP) system, which is responsible for authenticating users and managing their credentials. Part of these steps include defining an **Audience URI**, which specifies the intended recipient of a SAML assertion about a user's authentication. The configuration of an Audience URI depends on your IdP. See the following list of supported IdPs for specific instructions.

{: .note}
If your Audience URI is not configured correctly, Security Assertion Markup Language (SAML) assertions used for authentication will fail, preventing users from signing in using SSO.

## Supported IdPs

Firebolt allows you to sign in using federated identities. The SSO implementation supports the following IdPs:

- [Auth0]({% link Guides/security/sso/auth0.md %})
- [Okta]({% link Guides/security/sso/okta.md %})
- [OneLogin]({% link Guides/security/sso/onelogin.md %})
- [Salesforce]({% link Guides/security/sso/salesforce.md %})
- [PingFederate (Ping Identity)]({% link Guides/security/sso/pingfederate.md %})
- [Custom Identity provider]({% link Guides/security/sso/custom-sso.md %})

If your IdP is not listed but supports SAML2.0, contact the [Firebolt support team](mailto:support@firebolt.io). 

