---
layout: default
title: Deployment and Operational Guide
nav_order: 6
parent: Firebolt Core
has_children: true
---

# Deployment and Operational Guide

This document is for users who need to set up multi-node Firebolt Core clusters, customize single-node deployments with persistent storage, or require specific resource allocations beyond the scope of the [Get Started](./firebolt-core-get-started.md) guide.

Firebolt Core uses the official Docker image for all deployments. Simple local setups (see [Get Started](./firebolt-core-get-started.md)) require minimal configuration, while advanced multi-node deployments need additional customization. This page documents all configuration options and operational requirements.

## Overview

The Firebolt Core executable has some fixed expectations with respect to the runtime environment within its Docker container that need to be satisfied at all times. Specifically, it expects a fixed filesystem layout within the container, that remote nodes expose the relevant inter-node services on fixed ports, and that certain system resources are available.

### Filesystem

Within the Docker container, Firebolt Core exclusively operates within the `/firebolt-core` working directory. This directory contains the following relevant files and subdirectories.

* `/firebolt-core/firebolt-core` -- The main Firebolt Core executable which is executed as the container entrypoint. The executable accepts a small number of command-line arguments which are documented [below](#command-line-arguments).
* `/firebolt-core/config.json` -- The configuration file which is read by the Firebolt Core executable on startup. The Firebolt Core Docker image contains a default configuration file at this location which is suitable for starting a local single-node setup. You can inject your own configuration file by [mounting](https://docs.docker.com/engine/storage/) it at this location (see [below](#configuration-file)).
* `/firebolt-core/volume` -- The parent directory for all state which Firebolt Core writes during operation; this is the standard volume mount point used in the [Docker Compose](./firebolt-core-deployment-compose.md) and [Kubernetes setups](./firebolt-core-deployment-k8s.md); users should either provide a [Docker storage mount](https://docs.docker.com/engine/storage/) for the entire `/firebolt-core/volume` directory, or exercise more fine-grained control by individually mounting the following subdirectories (see [below](#storage-mounts) for details).
  * `/firebolt-core/volume/diagnostic_data` -- The directory to which Firebolt Core writes diagnostic information such as log files and crash dumps. Providing a storage mount for this directory makes it easier to inspect this diagnostic information on the host system (see also [Troubleshoot Issues](./firebolt-core-troubleshooting.md)). None of the files in this directory capture any database state, so they don't necessarily have to be persisted.
  * `/firebolt-core/volume/persistent_data` -- The directory to which Firebolt Core writes all data that is required to persist the database state itself, i.e. the schema and contents of the database.
  * `/firebolt-core/volume/tmp` -- The directory to which Firebolt Core writes temporary data. This includes, for example, intermediate query results that operators might have to spill to disk under memory pressure. Even though this information is only temporary, providing a [Docker storage mount](https://docs.docker.com/engine/storage/) might still be beneficial (see [below](#storage-mounts) for details). None of the files in this directory capture any database state, so they don't necessarily have to be persisted.

Note that all of the above data is written separately by *each Firebolt Core node*. In other words, in order to persist the database state of a four-node Firebolt Core cluster the `/firebolt-core/volume/persistent_data` directory of all four Firebolt Core Docker containers needs to mounted in a suitable way.

### Network

Within the Docker container, the Firebolt Core executable exposes a number of endpoints on fixed ports. Except for the main HTTP query endpoint, these are only relevant for inter-node communication in multi-node deployments. Here, the Firebolt Core executable expects all remote nodes to expose these endpoints on the same fixed ports.

* Port `3473` -- The main HTTP query endpoint (see [Connect](./firebolt-core-connect.md)).
* Port `8122` -- HTTP health check endpoint (see [Troubleshooting](./firebolt-core-troubleshooting.md)).
* Port `5678` -- Inter-node communication channel for the distributed execution control plane. This channel is used, for example, when the leader node for a specific query wants to schedule distributed work on the follower nodes.
* Port `16000` -- Inter-node communication channel for the distributed execution data plane. This channel is used by the shuffle operators in distributed query plans to exchange intermediate query results between nodes.
* Port `1717` -- Inter-node communication channel for the storage service which keeps track of how the contents of managed tables are sharded across nodes.
* Port `3434` -- Inter-node communication channel for the storage service which keeps track of how the contents of managed tables are sharded across nodes.
* Port `6500` -- Inter-node communication channel for the metadata service which maintains schema information and coordinates transactions.

Firebolt Core contains a high-performance implementation of the shuffle operator that exchanges intermediate query results between nodes. In order to harness the full potential of a multi-node Firebolt Core cluster, there should be at least 10 GBit/s of network bandwidth available between the nodes with reasonably low latency (ideally below 5 milliseconds). Assigning more network bandwidth generally improves performance of shuffle-heavy queries up to at least 75 GBit/s. In order to avoid being bottlenecked by [limits on single-flow bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html), the shuffle operator in Firebolt Core will send data over multiple parallel TCP connections.

### System Resources

As briefly mentioned in [Get Started](./firebolt-core-get-started.md), Firebolt Core internally uses the `io_uring` kernel API for efficient network and disk I/O. This kernel API is blocked by the default [Docker seccomp profile](https://docs.docker.com/engine/security/seccomp/) and **needs to be explicitly allowed** when starting a Firebolt Core Docker container. There are two main ways in which this can be achieved.

1. Start the Docker container with `--security-opt seccomp=unconfined` to disable `seccomp` confinement entirely.
2. Define a custom `seccomp` profile which extends the default Docker profile to additionally allow the `io_uring_setup`, `io_uring_enter`, and `io_uring_register` syscalls. In this case, the Docker container should be started with `--security-opt seccomp=/path/to/custom/profile.json`.

In addition, Firebolt Core relies on the capabilities of `io_uring` to pin certain buffers in main memory to eliminate unnecessary copies at the boundary between kernel-space and user-space. The size of these buffers counts against the `RLIMIT_MEMLOCK` resource limit, which is usually set to a comparatively low default value when starting Docker containers. Therefore, we **recommend to explicitly specify** `--ulimit memlock=8589934592:8589934592` when starting Firebolt Core Docker containers to avoid errors during startup.

## Configuration

There are three primary ways in which a Firebolt Core cluster can be configured. The topology of the cluster itself is defined through a minimal global JSON [configuration file](#configuration-file) that needs to be made available for each node. The identity of an individual node is specified through a command-line argument passed to the Firebolt Core executable. Finally, data can be made persistent or available for inspection by using [Docker storage mounts](https://docs.docker.com/engine/storage/).

### Configuration File

As outlined above, the Firebolt Core executable reads a single configuration file on startup to determine the desired cluster topology. This configuration file needs to be made available as the `/firebolt-core/config.json` file within the Docker container, for example by using a [Docker storage mount](https://docs.docker.com/engine/storage/) to mount a configuration file from the host operating system into the Docker container (see also the [Docker Compose](./firebolt-core-deployment-compose.md) and [Kubernetes](./firebolt-core-deployment-k8s.md) deployment guides).

The configuration file itself should be a JSON file with the following contents.

```json
{
    "nodes": [
        {
            "host": "node-0-hostname-or-ip-address"
        },
        {
            "host": "node-1-hostname-or-ip-address"
        }
        // Further nodes ...
    ]
}
```

Each entry in the `nodes` array corresponds to one node in the desired Firebolt Core cluster and specifies the hostname or IP address under which it is reachable from the other nodes. Usually, it is preferable to specify hostnames and rely on DNS (e.g. provided by [Docker](https://docs.docker.com/engine/network/)) to resolve them to IP addresses.

The same configuration file should be passed to each Firebolt Core node within a cluster. The `--node` command-line argument (see [below](#command-line-arguments)) is used to specify which of the entries in the `nodes` array corresponds to the "current" node, and which ones are remote nodes.

Ensure that any hostnames specified in the nodes array are resolvable to the correct IP addresses by all other nodes in the cluster. In Docker environments, this can often be achieved using custom Docker networks and container hostnames.

### Command-Line Arguments

The Firebolt Core executable accepts the following command-line arguments. Since the Firebolt Core executable is configured as the default [entrypoint](https://docs.docker.com/reference/dockerfile/#entrypoint) of the Firebolt Core Docker image, you can simply pass these command-line arguments to the container and they will be forwarded to the executable (see also the [Docker Compose](./firebolt-core-deployment-compose.md) and [Kubernetes](./firebolt-core-deployment-k8s.md) deployment guides).

* `--node=NODE_INDEX` -- Specify the index of the current node within a multi-node cluster, defaults to zero. This index identifies the entry within the `nodes` array of the configuration file which corresponds to the current node. If the configuration file specifies `N` nodes, each of the node indexes from `0` to `N - 1` should be assigned to exactly one of the nodes within the cluster.
* `--version` -- Print the Firebolt Core version number and exit.

### Storage Mounts

As outlined above, [Docker storage mounts](https://docs.docker.com/engine/storage/) can be used to inject a configuration file into the Firebolt Core Docker containers, and to control where any persistent or temporary data is written by Firebolt Core. Some concrete examples of this are provided in the [Docker Compose](./firebolt-core-deployment-compose.md) and [Kubernetes](./firebolt-core-deployment-k8s.md) deployment guides; this section provides some general guidelines for such storage mounts.

A custom configuration file needs to be provided at `/firebolt-core/config.json` for each node of a multi-node Firebolt Core cluster. This file is read by the Firebolt Core executable exactly once during startup to determine the cluster topology. Therefore, the way in which this file is mounted is not performance-critial. 

The situation is different for the `/firebolt-core/volume/persistent_data` directory. Depending on the specific workload Firebolt Core reads and writes potentially large amounts of data to and from this directory. More specifically, the following data is written to `/firebolt-core/volume/persistent_data`.

* Schema information is persisted in  `/firebolt-core/volume/persistent_data/metadata_storage`. 
* Table data is persisted in `/firebolt-core/volume/persistent_data/layered_space` and `/firebolt-core/volume/persistent_data/local_space`, in a proprietary format which can currently only be read by Firebolt Core engines.

All of the above directories need to be made persistent between container restarts if your workload is using any schema objects such as (external) tables. Note that it is possible to use a Firebolt Core cluster as a stateless query execution engine, e.g. by exclusively processing data read from Iceberg tables. In this case, it is not strictly necessary to persist the above directories as there is no persistent state anyway. If your workload is using schema objects managed by Firebolt Core, the storage mount for the persistent data directory should have sufficiently high I/O throughput. Ideally, it should be backed by an SSD drive with at least 2 GB/s of read and write throughput. Higher I/O throughput is likely to improve query performance and especially table scan performance further.

Similarly, Firebolt Core might read and write large amounts of data from and to the `/firebolt-core/volume/tmp` directory even if your workload does not involve any schema objects managed by Firebolt Core. This can happen if query plan operators such as joins or aggregations spill intermediate results to disk in order to avoid running out of working memory. If you observe that your workload causes a lot of queries to spill, it might be beneficial to provide an SSD-backed storage mount with high I/O throughput (at least 2 GB/s) for the temporary data directory as well. Alternatively, you can increase the amount of available main memory to avoid spilling entirely. In either case, the any files written to the temporary data directory do not have to be persisted between container restarts. Firebolt Core also actively removes files that are no longer needed from this directory.

Finally, Firebolt Core writes some diagnostic information to the `/firebolt-core/volume/diagnostic_data` directory. Files in this directory do not necessarily have to be persistent between container restarts, but can be useful for [troubleshooting](./firebolt-core-troubleshooting.md).

* Log files are always written to `/firebolt-core/volume/diagnostic_data/logs`.
* Crash dumps are written to `/firebolt-core/volume/diagnostic_data/crash`.

## Annotated example

First, let's revisit and dissect the local single-node deployment example from [Get Started](./firebolt-core-get-started.md). Here, we executed the following shell command to start a single-node Firebolt Core cluster on the local machine.

```bash
docker run \
    --tty \
    --rm \
    --security-opt seccomp=unconfined \
    --ulimit memlock=8589934592:8589934592 \
    --publish 127.0.0.1:3473:3473 \
    ghcr.io/firebolt-db/firebolt-core:preview-rc
```

The individual command-line arguments to the `docker run` command serve the following purpose.

* `--tty` -- Allocate a pseudo-tty for the container. This causes Firebolt Core to write log messages to this tty in addition to the log files in `/firebolt-core/volume/diagnostic_data/logs`; these logs are necessary when troubleshooting and/or submitting a bug report.
* `--rm` -- Remove the container when it is stopped. This is done to avoid cluttering the local system.
* `--security-opt seccomp=unconfined ` -- Disable `seccomp` confinement so that Firebolt Core can use `io_uring`.
* `--ulimit memlock=8589934592:8589934592` -- Increase the `RLIMIT_MEMLOCK` resource limit to 8 GB so that Firebolt Core can pin I/O buffers in memory.
* `--publish 127.0.0.1:3473:3473` -- Publish the container port 3473, on which the HTTP endpoint is exposed, to port 3473 on localhost. Since this is a single-node deployment, we don't need to publish the ports for inter-node communication.
* `ghcr.io/firebolt-db/firebolt-core:preview-rc` -- The Docker image from which to start the container.

Note that the above example does not specify any storage mounts. Since we have specified the `--rm` command line argument to the `docker run` command, the container is immediately removed when it is stopped and any database state is lost. It would of course be possible to simply omit `--rm`, in which case the database state will persist across container restarts. However, this is rather inflexible since all state is still tied to this specific container. A more flexible approach is to specify a storage mount as follows.

```bash
docker run \
    --tty \
    --rm \
    --security-opt seccomp=unconfined \
    --ulimit memlock=8589934592:8589934592 \
    --publish 127.0.0.1:3473:3473 \
    --mount type=bind,src=/firebolt-core-data,dst=/firebolt-core/volume \
    ghcr.io/firebolt-db/firebolt-core:preview-rc
```

Here, we added the following command-line argument.

* `--mount type=bind,src=/firebolt-core-data,dst=/firebolt-core/volume` -- Mount the `/firebolt-core-data` directory on the host system at `/firebolt-core/volume` in the container. Any persistent data written by Firebolt Core will now end up in `/firebolt-core-data` on the host system.

An analogous approach can be used to provide a storage mount for the temporary data directory, or to inject a custom configuration file.

## Multi-node setups

Setting up a multi-node Firebolt Core cluster involves the following key considerations:

1.  **Shared Configuration File:** The *same* `config.json` file, listing all nodes in the cluster with their respective hostnames or IP addresses, must be mounted or made available at `/firebolt-core/config.json` within each container.
2.  **Unique Node Identification:** Each Firebolt Core container must be started with a unique `--node=NODE_INDEX` argument. This index tells the Firebolt Core executable which entry in the `nodes` array of the `config.json` file corresponds to itself.
3.  **Network Connectivity:** All nodes must be able to communicate with each other using the hostnames/IPs and fixed ports specified for inter-node communication (e.g., ports `5678`, `16000`, `1717`, `3434`, `6500`). This usually means configuring them on a shared network.
4.  **Persistent Storage per Node:** If data persistence is required, *each node* in the cluster needs its own dedicated persistent storage mount for its `/firebolt-core/volume` directory. Shared storage for this directory across multiple nodes is not supported.
5.  **System Resource Allocation:** The `io_uring` enablement (via `seccomp` profile) and `RLIMIT_MEMLOCK` increase (`--ulimit memlock`) must be applied to *each node* in the cluster.
6.  **Port Publishing:** Typically, the main HTTP query endpoint (port `3473`) might be published externally for client access, potentially from one or more designated query nodes. Inter-node communication ports are generally not exposed externally but used within the cluster network.

When deploying using [Docker compose](./firebolt-core-deployment-compose.md) or [Kubernetes](./firebolt-core-deployment-k8s.md), most of these considerations are already taken care of and you can focus on customising only specific aspects like resource allocation and topology.
