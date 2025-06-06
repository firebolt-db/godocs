---
layout: default
title: Deployment on Kubernetes
nav_order: 2
parent: Deployment and Operational Guide
---

# Deployment on Kubernetes

Firebolt Core can be deployed to a Kubernetes cluster (version 1.19 or newer) using the [provided Helm chart](https://github.com/firebolt-db/firebolt-core/tree/main/helm). This section provides a step-by-step guide to get a working deployment up and running.

## Prerequisites

Before you begin, ensure that you have the following installed and configured:

* A [Kubernetes](https://kubernetes.io/) cluster (v1.19+)
* `kubectl` command-line tool configured to access your cluster
* `helm` (v3+) installed on your local machine

## 1: Create a Dedicated Namespace

To isolate Firebolt Core resources from other workloads in your cluster, create a dedicated Kubernetes namespace:

```bash
kubectl create namespace firebolt-core
```

This will create a logical grouping for all resources related to Firebolt Core, making it easier to manage and clean up later.

## 2: Customize Helm Chart Values

The deployment is configured via Helm chart values. You can modify these by editing a `values.yaml` file or by setting them directly via the `--set` flag.

For example, to deploy a 3-node cluster, ensure the `nodesCount` value is set to `3`; the memory allocation and storage allocation should also be increased for any serious workload you are planning to run.
It is advised to not use the default `preview-rc` value for the `image.tag` and instead pick a released pinned version from the [GHCR repository](https://github.com/firebolt-db/firebolt-core/pkgs/container/firebolt-core).

Refer to the [Helm Chart README](https://github.com/firebolt-db/firebolt-core/blob/main/helm/README.md) for the complete list of configurable parameters, including resource limits, storage options, and networking settings.

## 3: Install the Helm Chart

Once your values are configured, install the chart into the `firebolt-core` namespace:

```bash
helm install helm/ --generate-name --namespace firebolt-core
```

The `--generate-name` flag lets Helm automatically generate a release name. If you prefer to specify one, you can use:

```bash
helm install firebolt-core helm/ --namespace firebolt-core
```

## 4: Verify the Deployment

After installation, verify that the Firebolt Core pods are up and running:

```bash
kubectl get pods -n firebolt-core
```

You should see output similar to the following, depending on your `nodesCount` value:

```
NAME                              READY   STATUS    RESTARTS   AGE
helm-1748880880-firebolt-core-0   0/1     Running   0          5m33s
helm-1748880880-firebolt-core-1   0/1     Running   0          5m33s
helm-1748880880-firebolt-core-2   0/1     Running   0          5m33s
```

If the pods are **not** in the `Running` state, check their logs and events for troubleshooting:

```bash
kubectl describe pod <pod-name> -n firebolt-core
kubectl logs <pod-name> -n firebolt-core
```

## 5: Querying locally

You can interact with Firebolt Core locally by port-forwarding the HTTP interface port (default: `3473`) from one of the pods to your local machine. This enables you to send SQL queries directly via `curl` without exposing the service externally. To do this, run:

```bash
kubectl port-forward pod/helm-1748880880-firebolt-core-0 3473:3473 -n firebolt-core
```

Replace `helm-1748880880-firebolt-core-0` with the name of one of the running Firebolt Core pods.

Once forwarded, you can issue SQL queries using `curl`, for example:

```
curl -s "http://localhost:3473" --data-binary "select 42";
```

This approach is particularly useful for local testing and debugging.

## 6. Operations

You might want to setup backups for the mounted storage volumes to prevent data loss, and monitor iops usage to avoid slowdowns and latencies.

### Scaling up/down
⚠️ changing the number of nodes is currently supported for clusters which are only reading data, without performing any write.
If you need to perform writes and change cluster size, it will also be necessary to erase the data volume.

### Changing resources

You can run `helm update` to apply changes to your cluster after changing resources like memory or CPU allocation; pods will be recreated as necessary.

Note that it is not possible to resize storage volumes this way.

### Updating Firebolt Core version

After changing the `image.tag` value to a more recent pinned version you can run a `helm update` to roll out the change to your Firebolt Core cluster.

### Additional Resources

* Kubernetes [Namespaces documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
* Helm [Quickstart Guide](https://helm.sh/docs/intro/quickstart/)
