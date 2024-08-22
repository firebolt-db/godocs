---
layout: default
title: JDBC
description: How to use the Firebolt JDBC driver
nav_order: 3
parent: Develop with Firebolt
has_toc: true
---

# JDBC driver
{:.no_toc}

Firebolt provides a [type 4](https://en.wikipedia.org/wiki/JDBC_driver#Type_4_driver_%E2%80%93_Database-Protocol_driver/Thin_Driver(Pure_Java_driver)){:target="_blank"} JDBC driver to connect to Firebolt from Java applications. The driver is released as open source software using a permissive Apache 2 license and can be browsed, forked, downloaded, and contributed to through its [GitHub repository](https://github.com/firebolt-db/jdbc){:target="_blank"}.

* Topic toC
{:toc}

## Download the JAR file

The Firebolt JDBC driver is provided as a JAR file and requires [Java 11](https://java.com/en/download/manual.jsp){:target="_blank"} or later. 

Download the Firebolt JDBC driver JAR file from the [GitHub Releases page](https://github.com/firebolt-db/jdbc/releases){:target="_blank"}.

## Adding the Firebolt JDBC driver as a Maven dependency

If you are using Apache Maven, you can configure and build your projects to use the Firebolt JDBC driver to connect to your Firebolt resources. To do this, add the JDBC driver as a dependency in your project **pom.xml** file by including a link to the [Firebolt Maven repository](https://central.sonatype.com/artifact/io.firebolt/firebolt-jdbc){:target="_blank"}.

See below for an example pom.xml file:

  {: .note}
  Be sure to replace `<version>3.1.0</version>` with the latest (highest) version number. You can identify the latest version by viewing the version history in the [Firebolt Maven Central repository](https://central.sonatype.com/artifact/io.firebolt/firebolt-jdbc){:target="_blank"}.
    
    <!-- pom.xml  -->
    
    <project ...>
           <dependency>
                	<groupId>io.firebolt</groupId>
                	<artifactId>firebolt-jdbc</artifactId>
                	<version>3.1.0</version>
           </dependency>
    </project>


## Adding the Firebolt JDBC driver as a gradle dependency

  {: .note}
  Be sure to replace `<version>0.00</version>` with the latest (highest) version number. You can identify the latest version by viewing the version history in the [Firebolt Maven Central repository](https://central.sonatype.com/artifact/io.firebolt/firebolt-jdbc){:target="_blank"}.

    /* build.gradle */
    
    repositories {
        mavenCentral()
    }
    
    dependencies {
        implementation 'io.firebolt:firebolt-jdbc:3.0.1'
    }

## Connecting to Firebolt with the JDBC driver

Connection details are provided to the Firebolt JDBC driver in a connection string. The string has the following format:

    jdbc:firebolt:<database>?<connection_params>

`<database>`<br/>
The name of the Firebolt database to connect to.

`<connection_params>`<br/>
A list of connection parameters following the standard [URL query string format](https://en.wikipedia.org/wiki/Query_string#Structure).

## Authentication

To authenticate, use a service account ID and secret.
A service account is identified by a `client_id` and a `client_secret`.
For compatibility with various external tools, `client_id` can be sent as `user` and `client_secret` as `password`.  
Learn how to generate an ID and secret [here](../managing-your-organization/service-accounts.md).

Here is an example of a connection details:

* URL that uses client_id/secret_id
  ```
    jdbc:firebolt:my_database?client_id=<client_id>&client_secret=<client_secret>&account=my_account&engine=my_database_general_purpose&buffer_size=1000000&connection_timeout_millis=10000
  ```

* URL that uses that omits authentication details that are passed in properties
  ```
  jdbc:firebolt:my_database?account=my_account&engine=my_database_general_purpose&buffer_size=1000000&connection_timeout_millis=10000`
  ```
  Connection properties:
  ```
  client_id=<client_id>
  client_secret=<client_secret>
  ```

* Minimal URL that sends all additional parameters in connection properties
  ```
  jdbc:firebolt:my_database
  ```
  Connection properties:
  ```
  client_id=<client_id>
  client_secret=<client_secret>
  account=my_account
  engine=my_database_general_purpose
  buffer_size=1000000
  connection_timeout_millis=10000
  ```

* Minimal URL that sends user and password (client_id and client_secret) using connection properties, omits engine name and therefore connects to default engine and relies on default values of other parameters
  ```
  jdbc:firebolt:my_database
  ```
  Connection properties:
  ```
  client_id=<client_id>
  client_secret=<client_secret>
  account=my_account
  ```

  {: .note}
  Since the connection string is a URI, make sure to [percent-encode](https://en.wikipedia.org/wiki/Percent-encoding){:target="_blank"} any reserved characters or special characters used in parameter keys or parameter values.

### Available connection parameters

The table below lists the available connection parameters that can be added to the Firebolt JDBC connection string. All parameter keys are case-sensitive.

| Parameter key                        | Data type  | Default value                               | Range           | Description                                                                                                                                                                                                                     |
|--------------------------------------| ---------- |---------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| client_id                            | TEXT     | No default value                            |                 | The Firebolt service account ID. **Required.**                                                                                                                                                                                  |
| client_secret                        | TEXT     | No default value                            |                 | The secret generated for the Firebolt service account. **Required.**                                                                                                                                                            |
| account                              | TEXT     | No default value                            |                 | Your Firebolt account name.  **Required.**                                                                                                                                                                                                   |
| database                             | TEXT     | No default value                            |                 | The name of the database to connect to. Takes precedence over the database name provided as a path parameter.                                                                                                         |
| engine                               | TEXT     | Default engine attached to chosen database |                 | The name of the engine to connect to.                                                                                                                                                          |
| buffer_size                          | INTEGER        | 65536                                       | 1 to 2147483647 | The buffer used by the driver to read the response from the Firebolt API, in bytes.                                                                                                                                   |
| connection_timeout_millis            | INTEGER        | 60000                                       | 0 to 2147483647 | The amount of time in milliseconds to wait to establish a connection with the server before the connection is considered failed. <br/>A timeout value of zero is interpreted as an infinite timeout.                  |
| max_connections_total                | INTEGER        | 300                                         | 1 to 2147483647 | The maximum total number of connections.                                                                                                                                                                              |
| socket_timeout_millis                | INTEGER        | 0                                           | 0 to 2147483647 | The socket timeout in milliseconds. This is the timeout for waiting for data -- the maximum period of inactivity between two consecutive data packets. A timeout value of zero is interpreted as an infinite timeout. |
| connection_keep_alive_timeout_millis | INTEGER        | 300000                                      | 1 to 2147483647 | Specifies how long to keep a connection with the server alive in the connection pool before closing it.                                                                                                                         |
| ssl                                  | BOOLEAN    | true                                        | true or false   | When set to true, connections use SSL / TLS certificates. This parameter also determines the port used by the driver. If true, it uses port 443. If false, it uses port 80.                                                     |
| ssl_mode                             | TEXT     | strict                                      | strict or none  | When set to strict, the certificate is validated to ensure it is correct. If set to none, no certificate verification is used.                                                                                                  |
| ssl_certificate_path                 | TEXT     | No default value                            |                 | The absolute file path for the SSL root certificate.                                                                                                                                                                            |


### System settings as connection parameters

In addition to the parameters specified above, any [system setting](../../Reference/system-settings.md){:target="_blank"} can be passed as a connection string parameter. For example, if you wanted to set a custom time zone, your connection string would be as follows:
    
    jdbc:firebolt:my_database?time_zone=UTC&<other_connection_params>
    
## Applying system settings using SET

In addition to passing system settings as connection string parameters, any [system setting](../../Reference/system-settings.md){:target="_blank"} can be passed to Firebolt as a `SET` command in SQL. Multiple `SET` statements can be passed at once as long as they immediately follow one after another separated by semicolons, as shown in the following example.

    SET time_zone = 'UTC';
    SET standard_conforming_strings = false;

## Full reference documentation

Complete reference documentation for the classes and methods implemented in the Firebolt JDBC driver can be found [here](https://docs.firebolt.io/jdbc/javadoc/).
