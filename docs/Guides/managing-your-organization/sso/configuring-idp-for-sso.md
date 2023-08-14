---
layout: default
title: Configuring your identity provider for SSO
description: Learn how to configure your identity provider to work with SSO authentication for Firebolt. 
nav_order: 8
parent: Setting up SSO authentication
grand_parent: Managing your organization
great_grand_parent: Guides
---

# Configure your IDP to work with Firebolt
The purpose of this document is to outline the required configuration steps in your identity provider to work with Firbeolt.

{: .caution}
Before creating a SAML integration in your IDP, it is required to configure the Audience URI; otherwise, SAML assertions will not pass, and SSO will not allow users to sign in.

Firebolt supports the following identity providers (IDPs):
- Okta
- OneLogin
- Custom

If your IDP is not on the above list but supports SAML 2.0, contact the Firebolt support team for further assistance. 

## Okta
Integration with Okta is made using SAML2.0, so configuration steps are similar to other SAML identity providers.

### Configure Okta application
1. In Okta Admin Console, go to Applications > Applications
2. Click Create App Integration
3. Select SAML 2.0 as the Sign-in method, click Next.
4. In general configuration fill in the following fields:
    - Single sign-on URL: This URL looks as https://id.app.firebolt.io/login/callback?connection=<org_name>-<provider>&organization=<organization_identifier> Contact Firebolt to get your organization_identifier. Example of the URL: https://id.app.firebolt.io/login/callback?connection=vsko-okta&organization=org_82u3nzTNQPA8RyoM
    - Audience URI (SP Entity ID): This a URI in the following format: `urn:auth0:<tenant_name>:<org_name>-<provider>`, where `<tenant_name>` is app-firebolt-v2, `<org_name>` is the name of organization provider and `<provider>` is the provider value set in Firebolt configuration step

		Example of audience:
        urn:auth0:app-firebolt-v2:vsko-okta

5. Save the configuration.
6. Open the details of the created app integration, and select SAML tab, click More details to expand additional information.
7. Copy the value for Identity Provider Single Sign-On URL and download the signing certificate.


Example: firebolt organization configuration to work with Okta:


Values for SQL to create the SSO connection are as follows:
ALTER ORGANIZATION vsko SET SSO = '{
  "signOnUrl": "https://vsko.okta.com/app/vsko_app_1/exk8kq6ikd3Is13KO4x7/sso/saml",
  "issuer": "okta",
  "provider": "okta",
  "label": "Okta Company App",
  "fieldMapping": {
    "given_name": "name",
    "family_name": "surname"
  },
  "certificate": "<certificate>",
}';


signOnUrl - Identity Provider Single Sign-On URL value copied during Okta setup
issuer - issuer value 
provider - IdP name, for instance ‘okta’
label - text that will appear on sign in form button. In case not provided, it will be defaulted to ‘<org_name>-<provider>’, for instance ‘acme-okta’ 
certificate - X.509 Certificate copied during OneLogin setup
field_mapping - additional fields to be mapped from SAML assertion, based on what was configured during Okta setup. For instance:
{
  "given_name": "name",
  "family_name": "surname"
}


## OneLogin
Integration with OneLogin is made using SAML2.0, so configuration steps are similar to other SAML identity providers.
1. Configure OneLogin application.

2. In OneLogin open Dashboard, and click Apps > Add Apps.
3. Search for SAML, and select SAML Test Connector (IdP w/attr).
4. Change the Display Name of an app and click SAVE. This is the name of the app that will appear in OneLogin Portal:

5. Open SSO tab and copy the value for SAML 2.0 Endpoint (HTTP). Note that we are not using logout endpoint at this time.

6. Click on the View Details link at the X.509 Certificate field and copy/download the certificate.
7. Open Configuration tab and fill in the following values:
- Audience - a URI in the following format: `urn:auth0:<tenant_name>:<org_name>-<provider>`, where
`<tenant_name>` is app-firebolt-v2, `<org_name>` is the name of organization, and `<provider>` is the provider value set in Firebolt configuration step. Example of audience: `urn:auth0:app-firebolt-v2:vsko2-onelogin`

- ACS (Consumer) URL Validator - a valid regular expression
		[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)

        This field is being used to ensure OneLogin posts the response to the correct URL, and it validates the ACS URL field.
- ACS (Consumer) URL and Recipient - the post-back URL for your organization. This is the url in the following format:
https://id.app.firebolt.io/login/callback?connection=<org_name>-<provider>&organization=<organization_identifier>.

The organization_identifier is needed to select correct organization during redirects. The authentication flow will fail if it is provided incorrectly or not provided.

Contact the Firebolt support team to retrieve your organization_identifier.

Example:
https://id.app.firebolt.io/login/callback?connection=vsko2-onelogin&organization=org_82u3nzTNQPA8RyoM

Configuration tab example:

Example: firebolt organization configuration to work with OneLogin:
Values for SQL to create the SSO connection are as follows:
ALTER ORGANIZATION vsko SET SSO = '{
  "signOnUrl": "https://vsko-test.onelogin.com/trust/saml2/http-post/sso/aa",
  "issuer": "onelogin",
  "provider": "onelogin",
  "label": "OneLogin Company App",
  "fieldMapping": {
    "given_name": "name",
    "family_name": "surname"
  },
  "certificate": "<certificate>",
}';


org_name - name of the organization in Firebolt
signOnUrl - SAML 2.0 Endpoint (HTTP) value copied during OneLogin setup
issuer - issuer value 
provider - IdP name, for instance ‘onelogin’
label - text that will appear on sign in form button. In case not provided, it will be defaulted to ‘<org_name>-<provider>’, for instance ‘acme-onelogin’ 
certificate - X.509 Certificate copied during OneLogin setup
field_mapping - additional fields to be mapped from SAML assertion, based on what was configured during OneLogin setup. For instance:
{
  "given_name": "name",
  "family_name": "surname"
}


And this corresponds to the following setup in OneLogin, where name/surname in OneLogin corresponds to values in JSON:





## Custom

To use a SAML 2.0 compliant service or application as your IDP for single sign on (SSO) with FIrebolt, complete the following steps:
1. In the service/application interface, define a custom SHA-256 application for Firebolt. Follow the specific instructions of the service/application in order to define such a custom application.
2. In the interface, create a user for each end-user that needs to access Firebolt. When creating the users make sure to specify the email address for those users. Firebolt using those email addresses to create the corresponding logins in Firebolt. See [setting up SSO] for more information.
3. Obtain values for Audience URI and ACS (Consumer) URL to use in the IDP setup from Firebolt.
4. Obtain the SSO URL (This is the URL endpoint to which Firebolt sends the SAML requests.) and certificate (used to verify the communication between the IDP and Firebolt) for your custom IDP. You will need the SSO URL value and certificate in order to set [set up SSO].

