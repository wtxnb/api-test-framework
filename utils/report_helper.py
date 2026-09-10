"""本地生成 Allure 报告的小工具（需要已安装 allure 命令行）。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "reports" / "allure-results"
OUTPUT = ROOT / "reports" / "allure-report"


def generate():
    if not RESULTS.exists():
        print("未找到 allure-results，请先运行 pytest")
        sys.exit(1)
    subprocess.run(
        ["allure", "generate", str(RESULTS), "-o", str(OUTPUT), "--clean"],
        check=True,
    )
    print(f"报告已生成: {OUTPUT}/index.html")


if __name__ == "__main__":
    generate()
