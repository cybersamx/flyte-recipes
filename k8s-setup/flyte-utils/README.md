# Flyte Utils

This is a Docker image that designed to be run interactively in a k8s cluster running flyte. It contains programs to help interact and diagnose flyte, and its jobs and dependencies. 

1. Build the docker image that has python, awscli, and postgres client.

   ```shell
   docker build -t cybersamx/flyte-utils -f Dockerfile .
   ```

1. Push the image to Docker Hub.

   ```shell
   docker push cybersamx/flyte-utils
   ```

1. Run kubectl to find out the cluster ip address of minio.

   ```shell
   kubectl get all -n flyte
   NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   service/minio                 ClusterIP   10.96.132.61    <none>        80/TCP     12h
   service/postgres-postgresql   ClusterIP   10.96.184.240   <none>        5432/TCP   8h
   ```

1. Run flyte-utils in a k8s cluster. Once in a shell session, connect to minio and postgres.

   ```shell
   kubectl run shell --rm -it --image cybersamx/flyte-utils -- bash
   root@shell:~# aws --endpoint-url http://10.96.132.61 s3 ls
   2024-04-20 06:24:46 data
   2024-04-20 19:35:51 metadata
   root@shell:~#
   root@shell:~# psql -h 10.96.184.240 -U postgres -d postgres
   Password for user postgres:
   psql (13.14 (Debian 13.14-0+deb11u1), server 11.5 (Debian 11.5-3.pgdg90+1))
   Type "help" for help.
   postgres=#
   ```

## Notes

* If we want a generic shell running in a k8s cluster, we can run the following: `kubectl run shell --rm -it --image ubuntu -- bash`
* If we want to run a generic shell as a docker container, we can run the following: `docker run --name shell --rm -it ubuntu /bin/bash`

## Journal

Journal notes from past work. They can be removed later.


1. Run the local registry that the local k8s cluster can pull from (doesn't quite work).

   ```shell
   docker run -d -p 5555:5000 --name registry registry:latest
   ```

1. Build the docker image that has python, awscli, and postgres client.

   ```shell
   docker build -t flyte-utils -f Dockerfile .
   ```

1. Tag the image to the name of the local registry.

   ```shell
   docker tag flyte-utils localhost:5555/flyte-utils
   docker push localhost:5555/flyte-utils
   curl localhost:5555/v2/_catalog
   ```

1. Run shell utils to verify services in k8s cluster.

   ```shell
   kubectl run shell --rm -it --image localhost:5555/flyte-utils -- bash
   ```
