"""测试数据加载：支持 YAML / JSON 两种格式，放在 test_data 目录。"""
import json
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).resolve().parent.parent / "test_data"


def load_yaml(name: str):
    with open(DATA_DIR / name, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(name: str):
    with open(DATA_DIR / name, "r", encoding="utf-8") as f:
        return json.load(f)
