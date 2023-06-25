# Setup for Flyte Sandbox

Setup instructions and notes for running Flyte cluster in sandbox mode (aka `flytectl demo start`). It's basically 1 container that is comprised of all Flyte components and dependencies (including minio and postgres) as 1 big container.

Use this for starting out and running a Flyte cluster locally.

Currently, the instructions are for the Mac.

## Setup

1. Install `Docker Desktop`.

   ```shell
   brew install --cask docker
   ```
   
   Launch Docker Desktop and ensure we have the following settings:
   
   | Settings          | Values       |
   |-------------------|--------------| 
   | # CPUs            | At least 4   |
   | Memory            | At least 4GB |
   | Enable Kubernetes | Disabled     |

   Please don't enable kubernetes, `flytectl demo start` will set up and enable k8s automatically. To set up Flyte, please refer to the setup wiki for k8s.

1. Install `flytectl`, which we need to interact with the control plane for managing a flyte cluster.

   ```shell
   brew install flyteorg/homebrew-tap/flytectl
   # Alternatively
   curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
   ```
   
1. Set up a virtual environment for this project.

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

1. Install the Flyte SDK, `flytectl`.

   ```shell
   pip install -r requirements-tools.txt
   ```

1. Always find it hard to type `flytectl` in full. So do this in shell or/and your shell config.

   ```shell
   alias fc=flytectl
   alias pf=pyflyte
   ```
   
1. While working this project, launch the flyte cluster locally. Might take a while to start if you running this the first time.

   ```shell
   flytectl demo start
   ```

1. Run this in shell and update in your shell config.

   ```shell
   export FLYTECTL_CONFIG=~/.flyte/config-sandbox.yaml
   ```
   
1. Run `docker ps` and you should see a container named `flyte-sandbox` running.

1. To stop the flyte cluster.

   ```shell
   flytectl demo teardown
   ```

## Notes

* Tried using Rancher Desktop as the underlying docker engine for `flytectl demo start`, but ran into problems. We will run `flyte demo start` in `Rancher Desktop` later. 

## FAQ

1. Workflow failed with `USER::OpenBLAS WARNING - could not determine the L2 cache size`.

   Increase virtual machine resources. See above, at least 4 vCPUs and 4GB memory.

1. Docker doesn't have sufficient memory available.

   Prune the volumes in your docker environment.

   ```shell
   docker volume prune
   ```

## Reference

* [FLyte Docs: Sandbox Deployment](https://docs.flyte.org/en/latest/deployment/deployment/sandbox.html)
