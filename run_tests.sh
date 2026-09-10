#!/usr/bin/env bash
set -e
pip install -r requirements.txt
pytest
echo "生成 Allure 报告（需已安装 allure 命令行）..."
python utils/report_helper.py
