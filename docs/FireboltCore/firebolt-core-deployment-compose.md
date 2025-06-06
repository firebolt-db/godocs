---
layout: default
title: Deployment using Docker Compose
nav_order: 1
parent: Deployment and Operational Guide
---

# Deployment using Docker Compose

You can use Docker Compose to create a multi-node Firebolt Core deployment.
This is useful if you have multiple hosts that are already on the same network (for example, your home or office LAN); if you have remote machines available on Kubernetes, see [Deploy using Kubernetes](./firebolt-core-deployment-k8s.md) instead.

For the purpose of this example, we will assume that the hostnames of these machines are `example-node-a` and `example-node-b`; you can use an arbitrary number of nodes, but beware that you cannot add them later after the cluster has been started.

## Configuration
On both `example-node-a` and `example-node-b` you will need to clone the repository:
```bash
git clone https://github.com/firebolt-db/firebolt-core
```

And then create the following `config.json` file.

```json
{
    "nodes": [
        {
            "host": "example-node-a"
        },
        {
            "host": "example-node-b"
        }
    ]
}
```

Persistence is already enabled by default on each of the nodes through the mounted local directory `firebolt-core-data`.

## Node 0 start

Run:
```bash
docker compose up
```
On the cloned repository directory on `example-node-a`; this will start the first Firebolt Core node. Please note that attempting to send queries to its HTTP endpoint will return an HTTP 500 error since the cluster is not yet healthy - this is expected because the second node is not yet up and running.

## Node 1 start

Run:
```bash
NODE=1 docker compose -f compose.yaml -f compose.nodeN.yaml up
```
On the cloned repository directory on `example-node-b`; this will start the second Firebolt Core node.

## Further nodes

For any further node repeat the steps for node 1 and use an incremental `NODE` (e.g. 2 and so on).

## Querying

You can now query each node independently, directly utilizing their resources:
```bash
curl -s "http://example-node-a:3473" --data-binary "select 42";
curl -s "http://example-node-b:3473" --data-binary "select 42";
```

Continue reading: [Deploy using Kubernetes](./firebolt-core-deployment-k8s.md)