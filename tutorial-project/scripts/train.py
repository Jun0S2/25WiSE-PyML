import argparse

from core.config.config import GlobalConfig, ModelConfig
from core.utils.utils import create_experiment_subdir, generate_run_id, save_config_to_json


def run(global_cfg: GlobalConfig, model_cfg: ModelConfig) -> None:
    print(global_cfg)
    print(model_cfg)

    run_id = generate_run_id()
    exp_dir = create_experiment_subdir(global_cfg, run_id)
    print(f"Experiment directory created at: {exp_dir}")

    # We don't save `GlobalConfig` b/c this is usually not necessary
    # for reproduciblity.
    save_config_to_json(model_cfg, exp_dir / "config.json")


def main() -> None:
    model_cfg = ModelConfig()

    # CLI interface: helpful for deploying many runs via a loop (e.g., on a HPC)
    # Alternative workflow: wrapper .py module that creates config objects
    #   (e.g., selective grid search that is more complex than a bash
    #   for-loop) and calls `run`
    # Note: we could alternatively create the CLI args dynamically
    #   (→ less redundancy, but perhaps also less readability)
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", dest="seed", type=int, default=argparse.SUPPRESS)
    parser.add_argument("--learning-rate", dest="learning_rate", type=float, default=argparse.SUPPRESS)
    parser.add_argument("--batch-size", dest="batch_size", type=int, default=argparse.SUPPRESS)
    parser.add_argument("--n-epochs", dest="n_epochs", type=int, default=argparse.SUPPRESS)
    parser.add_argument(
        "--hidden-layer-sizes",
        dest="hidden_layer_sizes",
        type=int,
        nargs="+",
        default=argparse.SUPPRESS,
    )
    args = parser.parse_args()

    # Note: if we overwrite values in `ModelConfig`, we cannot use a frozen
    # dataclass.
    for key, value in vars(args).items():
        if not hasattr(model_cfg, key):
            continue
        if isinstance(getattr(model_cfg, key), tuple):
            setattr(model_cfg, key, tuple(value))
        else:
            setattr(model_cfg, key, value)

    # We currently don't allow overwrites to `GlobalConfig`. That is b/c
    # `GlobalConfig` usually stays constant across runs.
    # If we'd want to overwrite, one way is via using overwrites from
    # environment variables
    global_cfg = GlobalConfig()

    run(global_cfg, model_cfg)


if __name__ == "__main__":
    main()
