# PyML project (second part): coding exercise

## Relation to part one of the project

This exercise builds on part one of the project. Note that this repository contains **one possible solution** to the project's first part. However, there are many more suitable implementations (some perhaps even better than the sample solution!). We encourage you to develop your own solution while using our instructions as "prompts" for your own learning.

## Layout

Note that we **very slightly** refactored the first part's layout (relative to the task description from `first-part/` that we had originally published) to suit the later project parts better. The layout idea is as follows:

- `core/` (previous `src/`) will contain the code to train and evaluate our future diffusion model. It now contains `config/` as a subfolder. Each run will create a run directory to collect artifacts. Think of this like a package (like `torch` but for a different purpose).
- `scripts/` is the "entrypoint" that imports our `core` package and starts training or evaluation runs.
- `results/` will allow us to evaluate **multiple** run paths (that each collect training and evaluation artifacts for a single model configuration, respectively). For example, the modules in this directory could create a plot that compares model performance over different training configurations.

## Tasks

This part will still focus on infrastructure. Only the third (future) part of the project will cover our diffusion model.

We provide a lot of guidance to help you. If you feel that this guidance is too rigid for you (e.g., because you are an experienced programmer), feel free to deviate.

### Results handling

- In `core/utils/results.py`, write the following abstractions for handling experimental results:
  - Context: We already implemented `core/config/ModelConfig`, which specifies training and evaluation hyperparameters. We need this to deploy new training or eval runs, where eval runs operate on already trained models (e.g., sampling a diffusion model). We now want to build abstractions that can wrap results of our experiments.
  - `ResultMetadata` should represent the metadata of an experiment result, e.g., it could contain attributes representing a name (like `sampling`), the number of sampling steps (like `n_steps`), or the number of samples (like `n_samples`). This abstraction should be immutable after instantiation (e.g., to use it as a key in a dict).
  - `ScalarResult` should hold (scalar) results, specifically a `mean` and an `error` (think of the latter as an error bar).
  - `ResultRecord` should be a wrapper around `ResultMetadata` and `ScalarResult`
  - `ResultCollection` should be an iterable (supports `for`) for several `ResultRecord` objects. This will help us to iterate over results from several runs using the modules in the (future) `results/` directory.
  - For all above abstractions, ensure that they evaluate to readable strings via `print`. Furthermore, the above objects should contain type annotations, including for return types.
- Build an abstraction that takes `ResultRecord` **and** the run directory `Path` (e.g., the subdir returned by `create_experiment_subdir`) as input and (a) prints the results in a readable format to stdout and (b) optionally also saves them in our "run directory" (on the filesystem), e.g., via JSON. The latter might be a bit tricky. Feel free to use AI or skip for now.

### Meter

In `core/utils/meters.py`, write a `Meter` class that will allow us to track some metric over several iterations (e.g., to compute the average loss over several iterations, even if the last batch is smaller than the first batches, i.e., we cannot just naively use a list and average):

- `Meter` should work with several measures simultaneously (e.g., loss and other diagnostics measures, e.g., gradient norms).
- `__init__` initializes a datastructure to handle intermediate results for multiple measures.
- `update()` adds new values in a memory-efficient way, i.e., **not** by (excessively) appending to a list.
- `mean()` and `error()` compute the mean and standard error (SE = sqrt(variance) / sqrt(number of samples) = std / sqrt(n))
- It has a function that automatically creates a `ScalarResult` instance with the `mean` and `error` values given a specific measure.

### Timer

- In `core/utils/utils.py`, write a decorator and/or context manager that can be used to measure the execution time of a function.

### Training & evaluation scaffolding

- In `core/diffusion/model.py`, write a very simple neural network (subclassing `nn.Module`) that simply returns its input when called (an identity function). Its `__init__` should take `ModelConfig` (see the first project part) as input, but it does not have to do anything with it yet. Later, this will help initialize the neural network layers.
- In `core/diffusion/train.py`, write a function `train_diffusion_model` that takes as input the `ModelConfig` and the `run_path` (where we will store experimental artifacts):
  - In the function, create an instance of our model and pass "dummy" tensors through the model.
  - Furthermore, create a "dummy" result and "log" it.
  - The function returns the model instance.
  - The function is called by `scripts/train.py`
- In `core/diffusion/eval.py`, write a class `Evaluator`. The `__init__` takes the `ModelConfig` and the `run_path` as input. The function `evaluate()` will carry out evaluation. Similar to `core/diffusion/train.py`, populate this module with "dummy" computation and call it from `scripts/eval.py`.
- Use the timer decorate/context manager (see above) to measure the execution time of training and evaluation, respectively (currently, this should be ~0s each).
