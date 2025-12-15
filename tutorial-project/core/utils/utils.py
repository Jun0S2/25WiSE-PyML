import json
import uuid
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

from core.config.config import GlobalConfig, ModelConfig


def save_config_to_json(cfg: ModelConfig, path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(asdict(cfg), f, indent=4, ensure_ascii=False)


def load_config_from_json(path: str | Path) -> ModelConfig:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    defaults = ModelConfig()
    normalized = {}
    for key, value in data.items():
        default_value = getattr(defaults, key, None)
        if isinstance(default_value, tuple) and isinstance(value, list):
            value = tuple(value)
        normalized[key] = value
    return ModelConfig(**normalized)


def generate_run_id() -> str:
    ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%S")
    return f"{ts}_{uuid.uuid4().hex}"


def create_experiment_subdir(global_cfg: GlobalConfig, run_id: str) -> Path:
    base = Path(global_cfg.dir_experiments)
    base.mkdir(parents=True, exist_ok=True)
    sub = base / run_id
    sub.mkdir()
    return sub
