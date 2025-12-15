from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from core.config.config import GlobalConfig, ModelConfig
from core.utils.utils import load_config_from_json


@dataclass
class Run:
    id: str
    path: Path
    config: ModelConfig


class ResultsDatabase:
    def __init__(self, *, config: GlobalConfig, dir_experiments: Path | None = None):
        self.dir_experiments = Path(dir_experiments) if dir_experiments is not None else config.dir_experiments

        self.results: dict[str, Run] = {}
        for config_path in self.dir_experiments.rglob("config.json"):
            run_config = load_config_from_json(config_path)
            run_dir = config_path.parent
            run_id = run_dir.name
            self.results[run_id] = Run(id=run_id, path=run_dir, config=run_config)

    def __iter__(self) -> Iterator[tuple[str, Run]]:
        return iter(self.results.items())

    def __repr__(self) -> str:
        return f"ResultsDatabase(dir_experiments={self.dir_experiments}, runs={len(self.results)})"


def main() -> None:
    database = ResultsDatabase(config=GlobalConfig())
    print(database)


if __name__ == "__main__":
    main()
