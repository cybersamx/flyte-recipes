# Flyte Utils

This is a Docker image that designed to be run interactively in a k8s cluster running flyte. It contains programs to help interact and diagnose flyte, and its jobs and dependencies. 

1. Build the docker image that has python, awscli, and postgres client.

   ```shell
   docker build --platform linux/amd64 -t cybersamx/flyte-utils -f Dockerfile .
   ```

1. Push the image to Docker Hub.

   ```shell
   docker push cybersamx/flyte-utils
   ```

1. Run kubectl to find out the cluster ip address of minio.

   ```shell
   kubectl get all -n flyte
   NAME               TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
   service/minio      NodePort   10.96.248.252   <none>        9000:30084/TCP,9001:30088/TCP   19m
   service/postgres   NodePort   10.96.109.127   <none>        5432:30089/TCP                  20m
   ```

1. Run flyte-utils in a k8s cluster. Once in a shell session, connect to minio and postgres.

   ```shell
   kubectl run shell --rm -it --image cybersamx/flyte-utils -- bash
   root@shell:~# aws --endpoint-url http://minio.flyte.svc.cluster.local s3 ls
   2024-04-20 06:24:46 flyte
   root@shell:~#
   root@shell:~# psql -h postgres.flyte.svc.cluster.local -U flyte -d flyte
   Password for user flyte:
   psql (13.14 (Debian 13.14-0+deb11u1), server 11.5 (Debian 11.5-3.pgdg90+1))
   Type "help" for help.
   flyte=#
   ```

## Troubleshooting

Some common commands to troubleshoot.

```shell
$ # Connect to a port
$ nc -z -v minio.flyte.svc.cluster.local 9000
$ # HTTP connect to a port
$ curl -Iv http://minio.flyte.svc.cluster.local:9000
```

## Notes

* If we want a generic shell running in a k8s cluster, we can run the following: `kubectl run shell --rm -it --image ubuntu -- bash`
* If we want to run a generic shell as a docker container, we can run the following: `docker run --name shell --rm -it ubuntu /bin/bash`
