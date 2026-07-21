from importlib.util import find_spec
from pathlib import Path
import sys


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    checks = []
    for package in ("flask", "pandas", "pytest"):
        checks.append((f"Python包：{package}", find_spec(package) is not None))
    for relative in (
        "app.py",
        "README.md",
        "requirements.txt",
        "services/data_service.py",
        "services/qa_service.py",
        "templates/dashboard.html",
        "templates/assistant.html",
        "tests/test_app.py",
        "data/overall_metrics.csv",
        "data/category_analysis.csv",
        "data/segment_analysis.csv",
    ):
        checks.append((f"文件：{relative}", (root / relative).is_file()))
    for label, ok in checks:
        print(f"[{'通过' if ok else '失败'}] {label}")
    failed = [label for label, ok in checks if not ok]
    print(f"\n检查目录：{root}")
    if failed:
        print(f"环境检查未通过：{len(failed)}项失败。")
        return 1
    print("环境检查通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
