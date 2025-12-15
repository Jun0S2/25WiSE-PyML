# Comments

As written in the task description: other solutions can be equally valid (if not better). The goal of this project is to prompt you to think about trade-offs between different design patterns in Python.

## `config.py`: `GlobalConfig`

`GlobalConfig` specifies configuration that is invariant to the hyperparameters of your (future) ML model.
For example, this includes the path to the data. It could also specify the frequency (over epochs) with which we want to save checkpoints fo the weights of **any** future model during training.

> Q: Why are we using a frozen dataclass for `GlobalConfig`?

Using a frozen dataclass ensures that the configuration is immutable, e.g., we cannot accidentally change them during runtime and you can use the config as a key in a dict.
Making the dataclass frozen is not strictly necessary here and mostly done for practice.

> Q: Could we use module-level constants or global variables instead?

Yes!
However, using classes can be helpful to encapsulate similar configuration and avoid to pollute scopes with too many objects.
Furthermore, classes have the advantage that we can define methods on their data attributes.

> Q: Could we use .env files instead?

Yes, e.g., you could use the library `python-dotenv` to load them as environment variables.
This is a common approach for handling sensitive information such as API keys and database credentials.
Note that .env files do not support type annotations and have less flexiblity than classes.
Note that you can generally combine dataclasses and `.env` files in your project.

> Q: What other ways exist to specify configuration?

There exist many libraries that define abstractions over model configurations. However, these add additional dependencies to your project, which hints at a trade-off.

## `config.py`: `ModelConfig`

`ModelConfig` holds model-specific configuration values such as training hyperparameters and model architecture details.

> Q: Why are we using a dataclass for `ModelConfig`?

A dataclass improves readability, e.g., we have to write less boilerplate code:

- We can specify all attributes as static class attributes (→ few lines of code). The dataclass automatically creates a corresponding `__init__`, which allows intializing the dataclass with differing values.
- The dataclass decorator automatically generates a `__repr__`, so we can `print` instances in a readable fashion.
- Dataclasses also have further benefits, e.g., optional immutability (via the `frozen` parameter, see above) and the ability to easily evaluate equality via elementwise attribute comparison (via an automatically generated `__eq__`).

> Q: Could we use a dictionary instead?

Dictionaries are a simpler object. Whether it is sufficient depends on the context, i.e., how much you benefit from the additional complexity that dataclasses offer (see above).
For example, dictionaries are limited in terms of type annotations.

> Q: Why do we put everything in a single `ModelConfig` class?

Imposing a hierarchical structure on model configuration (e.g., via several classes such as `TrainingConfig` and  `ModelArchitectureConfig` that define different parts of the model configuration) adds complexity.
This is helpful if it helps you to better control the degrees of freedom in your project.
Given that our project is currently relatively small, the additional overhead usually outweighs the advantages.
