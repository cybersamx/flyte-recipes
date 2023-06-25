# Official Example

This is a clone of [Flyte Official Example Code](https://docs.flyte.org/projects/cookbook/en/latest/index.html#creating-a-workflow).

## Setup

1. Install packages

   ```shell
   pip install -r requirements.txt
   ```
   
1. Run the program.

   ```shell
   pyflyte run flyte-demo.py training_workflow --hyperparameters '{"C": 0.1}'
   ```

1. Run the workflow in the cluster and then go to <http://localhost:30080/console/projects/flytesnacks/domains/development/executions>

   ```shell
   pyflyte run --remote flyte-demo.py training_workflow --hyperparameters '{"C": 0.1}'
   ```
