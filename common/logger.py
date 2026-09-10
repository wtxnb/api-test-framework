"""统一日志工具，输出到控制台，便于本地调试与 CI 日志查看。"""
import logging
from typing import Optional


def get_logger(name: str = "api_test") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        logger.addHandler(ch)
        logger.propagate = False
    return logger
