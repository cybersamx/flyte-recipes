# Flyte on Local Kubernetes Cluster

Install

* Docker Desktop or Rancher Desktop as a container engine
* Local multi-node kubernetes cluster using `kind`. 
* Minio emulating an object storage for flyte.
* Postgres as an application database for flyte.
* Flyte itself.

## Setup

Run Docker Desktop without k8s enabled. We will use kind as our k8s engine.

### Install Kind

Make our local k8s cluster multi-node. Kind creates a multi-node k8s cluster by running each node as a docker container.

1. Install kind.

   ```shell
   brew install kind
   ```
   
1. Create a kind cluster.

   ```shell
   kind create cluster --config=kind-cluster-config.yaml
   ```

1. List all kind clusters.

   ```shell
   kind get clusters
   ```

> **Note**
>
> To delete a kind cluster.
> 
> ```shell
> kind delete cluster --name kind
> ```


### Create Namespace

1. Create namespace `flyte` to put the flyte application and its dependencies.

   ```shell
   kubectl create ns flyte
   ```


### Install Postgres


1. Install postgres.


   ```shell
   kubectl apply -f postgres.yaml
   kubectl get all -n flyte
   ```

1. Verify that postgres is installed by setting port forwarding for the postgres service and then running psql.


   ```shell
   kubectl port-forward svc/postgres 5432:5432 -n flyte
   psql -h localhost -U flyte -d flyte
   ```


### Install Minio

1. Install minio.


   ```shell
   kubectl apply -f minio.yaml
   kubectl get all -n flyte
   ```

1. Verify that minio is installed by setting port forwarding for the minio service.


   ```shell
   kubectl port-forward svc/minio 9000:9000 9001:9001 -n flyte
   ```

1. Launch a web browser and navigate to <http://localhost:9000>.


### Install Flyte

We will be installing flyte using helm .

1. Point to a helm repo, from where the flyte chart can be downloaded.

   ```shell
   helm repo add flyteorg https://flyteorg.github.io/flyte
   ```
   
1. Install flyte via helm (assuming we have already created the k8s namespace `flyte`).

   ```shell
   helm install flyte-backend flyteorg/flyte-binary -n flyte --values flyte-values.yaml
   kubectl get all -n flyte
   ```

1. Set port forwarding so that we can access flyte consoles.

   ```shell
   $ kubectl get svc -n flyte
   NAME                                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   flyte-backend-flyte-binary-grpc      ClusterIP   10.96.235.147   <none>        8089/TCP   22h
   flyte-backend-flyte-binary-http      ClusterIP   10.96.189.119   <none>        8088/TCP   22h
   flyte-backend-flyte-binary-webhook   ClusterIP   10.96.7.174     <none>        443/TCP    22h
   $ kubectl port-forward svc/flyte-backend-flyte-binary-http 8088:8088 -n flyte
   $ kubectl port-forward svc/flyte-backend-flyte-binary-grpc 8089:8089 -n flyte
   $ kubectl port-forward svc/minio 9000:9000 9001:9001 -n flyte
   ```
 
1. We need the system that runs `flytectl` to resolve `minio.flyte.svc.cluster.local`. So we need to enter the host to the hosts file.

   ```shell
   sudo vi /etc/hosts
   ```
   
   Add the following:

   ```
   127.0.0.1    minio.flyte.svc.cluster.local
   ```
  
1. Download `flytectl`.

   ```shell
   brew install flyteorg/homebrew-tap/flytectl
   ```

1. Initialize `flytectl` by connecting to the flyte server on k8s.

   ```shell
   $ flytectl config init --host localhost:8088
   $ vi ~/.flyte/config.yaml
   admin:
     # For GRPC endpoints you might want to use dns:///flyte.myexample.com
     endpoint: dns:///localhost:8089  # The grpc host 
     authType: Pkce
     insecure: true  # Change it to true as we don't have tls set up.
   ```

1. Run a test workflow.

   ```shell
   $ # Leave this project directory so that we can clone the repo separately.
   $ git clone https://github.com/flyteorg/flytesnacks
   $ cd flytesnacks
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install flytekit
   $ cd examples/baiscs
   $ pyflyte run --remote basics/hello_world.py hello_world_wf
   ```

1. Launch a web browser and navigate to <http://localhost:8088/console>.


### Clean-up

1. Uninstall flyte.

   ```shell
   helm uninstall flyte-backend -n flyte
   ```

## References

* [AWS CLI with Minio](https://min.io/docs/minio/linux/integrations/aws-cli-with-minio.html)
* [Kind Home Page](https://kind.sigs.k8s.io/)
* [Cetic Postgres Hem Chart](https://github.com/cetic/helm-postgresql)
* [Flyte the Hard Way](https://github.com/davidmirror-ops/flyte-the-hard-way/blob/main/docs/on-premises/single-node/002-single-node-onprem-install.md)
