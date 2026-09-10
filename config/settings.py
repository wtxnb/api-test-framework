"""全局配置加载：根据 TEST_ENV 环境变量读取对应环境的 YAML 配置。"""
import os
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent


def load_env_config(env_name: str | None = None) -> dict:
    """加载指定环境的配置文件，未指定时取 TEST_ENV（默认 dev）。"""
    env_name = env_name or os.getenv("TEST_ENV", "dev")
    path = BASE_DIR / "config" / "environments" / f"{env_name}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"环境配置文件不存在: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


ENV = load_env_config()
BASE_URL = ENV.get("base_url", "").rstrip("/")
TIMEOUT = ENV.get("timeout", 10)
DEFAULT_HEADERS = ENV.get("headers", {})
