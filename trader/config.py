"""Configuration loading. All strategy parameters come from config.yaml."""
import os
import yaml

_CONFIG = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path=None):
    global _CONFIG
    if _CONFIG is None or path is not None:
        with open(path or os.path.join(ROOT, "config.yaml"), "r", encoding="utf-8") as f:
            _CONFIG = yaml.safe_load(f)
    return _CONFIG


def state_dir():
    d = os.path.join(ROOT, "state")
    os.makedirs(d, exist_ok=True)
    return d


def db_path():
    return os.path.join(state_dir(), "trader.db")
