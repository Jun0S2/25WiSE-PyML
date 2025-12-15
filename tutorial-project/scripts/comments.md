# Comments

## `train.py`: argument parsing

`scripts/` serves as an entrypoint for training and evaluating our (future) ML model.
If we want to deploy only one run, we can simply adjust the configuration in `core/config/`.
However, we might want to publish our `core/` package (such that we cannot change its code anymore) or we may want to deploy several runs concurrently.
In this case, we require a mechanism to change the model hyperparameters outside the `core/` package.
In the sample solution, we use a CLI interface that explicitly repeats the parameters of the `core/config/ModelConfig` class. Using this CLI interface, we can (for example) deploy several runs via a for loop in a bash wrapper script (a typical simple workflow on HPC).

Though the above approach is readable, it adds redundancy between the CLI interface and the `core/config/ModelConfig` values, i.e., if we want to change a configuration parameter, we always need to remember to change it in both places.
There are a few alternatives that do not have this disadvantage:

- We can create the CLI interface dynamically from the config dataclasses. However, this can impair readability and maintanability because we must map names, types, etc. of the dataclasses to the `argparse` syntax, which might requires hard-coding specific mappings between both data types.
- We could build a new Python module that generates different `core/config/ModelConfig` objects and passes them to the main train function. Here, it would also be possible to save these objects in some queue (persistent on the FS) and have another process grap elements from the queue for deployment.
