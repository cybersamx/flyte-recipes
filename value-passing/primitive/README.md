# Primitive Passing

Passing primitive values between tasks.

## Setup
 
1. Run the program.

   ```shell
   pyflyte run primitive.py primitive
   ```

1. Run the workflow in the cluster and then go to <http://localhost:30080/console/projects/flytesnacks/domains/development/executions>

   ```shell
   pyflyte run --remote primitive.py primitive
   ```

## Reference

* [Flyte and Python Types](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/type_system/flyte_python_types.html)
