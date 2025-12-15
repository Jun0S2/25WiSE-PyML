# PyML project (first part): coding exercise

In this part, we will write infrastructure code while treating the ML part as a black box.
As always, you can break "rules" if you know what you are doing.
Remember that we want to write scalable, high-quality code, not to develop as fast as possible.

Use the `__name__ == "__main__"` idiom for any module that we may want to execute directly (as opposed to merely importing it). Wrap all relevant computation in functions, i.e., use scopes properly.

## config

- Create a `core/config/` dir.
- Create a file `core/config/config.py` for the default config:
  - Contains a blueprint for configurations parameters for **future** neural networks, e.g., `n_layers` or `learning_rate`.
  - Contains a **different** abstraction that contains model-agnostic config, e.g., an "experiment directory" for collecting experimental results later (e.g., `~/tu-berlin/2025-winter/pyml/project/exp/`)
- **Optionally** use further files like `core/config/__init__.py` or `core/config/.env`

## scripts

- Create a file `scripts/train.py`:
  - Imports the default config
  - Uses an `argparse` CLI interface that allows overwriting the default config.
  - Calls a `run` function with the config object.
- `run` function:
  - Prints the used config **in a readable format** to stdout
  - Calls a function from `core/utils/utils.py` that generates a run-specific subdirectory in the "experiment directory" (see `core/config/`). The subdir name is a unique ID that specifies the run's date/time & an additional unique string (for concurrent runs).
  - Saves the config into a file in the "experiment directory".

## results

- Create a file `results/database.py`:
  - Contains a datastructure representing one run. It should specify the `run_id`, `run_path`, and the config.
  - Contains a second datastructure that represents several runs.
  - Iterates over the "experiment directory" (see above) and loads all runs into the above datastructures.
