# Flyte on Local Kubernetes Cluster

Install

* Docker Desktop or Rancher Desktop as a container engine
* Local multi-node kubernetes cluster using `kind`. 
* Minio emulating an object storage for flyte.
* Postgres as an application database for flyte.
* Flyte itself.

## Setup

Run Docker Desktop with Kubernetes enabled.

### Install Kind

Make our local k8s cluster multi-node. Kind creates a multi-node k8s cluster by running each node as a docker container.

1. Install kind.

   ```shell
   brew install kind
   ```
   
1. Create a kind cluster.

   ```shell
   kind create cluster --config=cluster-config.yaml
   ```

1. List all kind clusters.

   ```shell
   kind get clusters
   ```

1. Delete a kind cluster.

   ```shell
   kind delete cluster --name kind
   ```

### Install Minio

1. Switch to the right k8s cluster.

   ```shell
   $ kubectl config use-context kind-kind
   $ kubectl config current-context
   kind-kind
   ```
   
1. Install krew.

   ```shell
   brew install krew
   ```
   
   Add the following and then source the shell config file.

   ```shell
   export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
   ```
   
1. Update kew with the latest plug-ins.

   ```shell
   $ kubectl krew update
   $ kubectl krew install minio
   $ kubectl minio version
   Kubectl-Plugin Version: v5.0.14
   ```

1. Install minio operator.

   ```shell
   $ kubectl minio init -o > minio-manifest.yaml
   $ vi minio-manifest.yaml
   $ kubectl apply -f minio-manifest.yaml
   ```

1. Validate that minio operator is successfully installed.

   ```shell
   kubectl get all -n minio-operator
   ```

1. Set port forwarding to access minio operator web console.

   ```shell
   kubectl minio proxy
   ```

### Create a Tenant

1. Create a kubernetes namespace called `flyte` to host all flyte related resources on k9s cluster.

   ```shell
   $ kubectl create ns flyte
   ```

1. Launch a web browser and navigate to <http://localhost:9090>.

1. Create a tenant with these settings. 

   ![Create minio tenant setup](images/minio-create-tenant-setup2.png)

1. Go to **Configure** and disable `Expose MinIO Service` and `Expose Console Service`. For now, we don't want these services exposed to the Internet.

1. Go to **Identity Provider**. Since this is for local, non-production use, change the credentials for the admin to `admin123` and `admin123` as the Access Key and Secret Key respectively.

1. Go to **Security**. Again, since this is for non-production use, disable `TLS` and `AutoCert` (for now).

1. CLick **Create** to create the tenant.

### Create a Bucket

1. Set up port forwarding for the tenant.

   ```shell
   $ # Set the local port to 9000 since minio-operator console is using 9090
   $ kubectl port-forward svc/minio-console 9000:9090 -n flyte
   $ # On another shell run the following
   $ kubectl port-forward svc/minio 8000:80 -n flyte
   ```

1. Launch a web browser and navigate to <http://localhost:9000>.

1. Log in with `admin123` and `admin123`.

1. Create a bucket with the name `data`.

1. Click **Create** to create the bucket.

### Test Minio

1. Configure aws cli for minio.

   ```shell
   aws configure --profile minio
   AWS Access Key ID [None]: admin123
   AWS Secret Access Key [None]: admin123
   Default region name [None]: us-east-1
   Default output format [None]:
   ```

1. Enable aws signature version 4 for minio.

   ```shell
   aws configure set default.s3.signature_version s3v4
   ```

1. List the buckets on minio.

   ```shell
   $ aws --profile minio --endpoint-url http://localhost:8000 s3 ls
   2024-04-19 23:24:46 data
   ```

## References

* [AWS CLI with Minio](https://min.io/docs/minio/linux/integrations/aws-cli-with-minio.html)
* [Kind Home Page](https://kind.sigs.k8s.io/)
