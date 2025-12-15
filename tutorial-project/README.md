# 1D Diffusion

## Install

Install via [Astral UV](https://docs.astral.sh/uv/):

```bash
uv venv
source .venv/bin/activate
uv sync --extra dev
```

## Install pre-commit hook for formatter & linter & static type checker

Install and run [pre-commit](https://pre-commit.com/):

```bash
pre-commit install
pre-commit run --all-files
```

Tip: use an AI agent to fix pre-commit problems

## Usage

Run training with optional overrides (see `python scripts/train.py --help` for available flags):

```bash
python scripts/train.py --learning-rate 0.05
```

Before running, point the paths in `core/config/config.py` (e.g., `dir_experiments`, `dir_data`) to writable locations on your machine.
