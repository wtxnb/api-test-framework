# API 接口自动化测试框架

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-8.3-red.svg)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/report-allure2-brightgreen.svg)](https://allurereport.org/)
[![CI](https://github.com/wtxnb/api-test-framework/actions/workflows/api-tests.yml/badge.svg)](https://github.com/wtxnb/api-test-framework/actions/workflows/api-tests.yml)

基于 **pytest + requests + Allure** 的轻量级接口自动化测试框架，支持多环境配置、数据驱动、统一断言封装，并通过 **GitHub Actions** 实现提交即自动跑测 + 自动生成 Allure 报告。

> 演示环境使用公开 API [JSONPlaceholder](https://jsonplaceholder.typicode.com)，克隆后替换 `config/environments/*.yaml` 中的 `base_url` 即可对接你自己的服务。

## 技术栈

| 维度 | 选型 |
| --- | --- |
| 测试框架 | pytest 8 |
| 请求库 | requests |
| 报告 | allure-pytest 2 |
| 数据格式 | YAML / JSON |
| 持续集成 | GitHub Actions |
| 配置管理 | 环境变量 + YAML 多环境 |

## 目录结构

```
api-test-framework/
├── config/                 # 配置层
│   ├── settings.py         # 读取环境变量选择环境
│   └── environments/       # dev / prod 多环境配置
├── common/                 # 公共能力
│   ├── logger.py           # 统一日志
│   ├── request_helper.py   # 请求封装 + Allure 附件
│   ├── assertions.py       # 断言封装（step 级）
│   └── data_loader.py      # 测试数据加载
├── core/
│   └── base_api.py         # API 资源基类（CRUD 语义化）
├── testcases/              # 测试用例
├── test_data/              # 测试数据（YAML/JSON）
├── utils/
│   └── report_helper.py    # 本地生成 Allure 报告
├── reports/                # 测试产物（报告）
├── .github/workflows/      # CI 配置
├── conftest.py             # 全局夹具
├── pytest.ini
└── requirements.txt
```

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行测试（默认 dev 环境）
pytest

# 3. 指定环境运行
TEST_ENV=prod pytest

# 4. 只跑冒烟用例
pytest -m smoke

# 5. 本地生成 Allure 报告（需先安装 allure 命令行）
python utils/report_helper.py
# 浏览器打开 reports/allure-report/index.html
```

## 设计亮点（简历可写）

- **分层架构**：配置 / 公共 / 核心 / 用例分层，结构清晰、易维护。
- **多环境隔离**：通过 `TEST_ENV` 一键切换 dev / prod，配置与代码解耦。
- **数据驱动**：用例参数从 YAML/JSON 加载，`@pytest.mark.parametrize` 复用。
- **断言即文档**：所有断言包裹在 Allure step 中，失败定位快。
- **请求全留痕**：请求/响应自动作为 Allure 附件，排查问题零成本。
- **CI 全自动**：push / PR 自动跑测并产出 Allure 报告，质量门禁可感知。
- **语义化 API 对象**：`BaseAPI` 把 CRUD 封装成 `list/get_by_id/create/update`，用例更贴近业务。

## 如何扩展到自己的项目

1. 在 `config/environments/dev.yaml` 把 `base_url` 改成被测服务地址。
2. 在 `testcases/` 下新建 `test_xxx.py`，用 `conftest` 提供的 `*_api` 夹具。
3. 测试数据放到 `test_data/`，用 `common.data_loader` 加载。
4. 提交代码，GitHub Actions 自动跑测并生成报告。

---

作者：wtxnb · 用于软件测试 / 测试开发方向求职作品集
