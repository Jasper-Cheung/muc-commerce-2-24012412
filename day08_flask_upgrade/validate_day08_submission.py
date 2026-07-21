from pathlib import Path
import ast
import re
import sys


REQUIRED_FILES = (
    "app.py",
    "README.md",
    "requirements.txt",
    "services/data_service.py",
    "services/qa_service.py",
    "templates/dashboard.html",
    "templates/assistant.html",
    "tests/test_app.py",
)


def count_tests(path: Path) -> int:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return sum(isinstance(node, ast.FunctionDef) and node.name.startswith("test_") for node in tree.body)


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    errors = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"缺少文件：{relative}")

    app_text = (root / "app.py").read_text(encoding="utf-8") if (root / "app.py").is_file() else ""
    service_text = (root / "services/data_service.py").read_text(encoding="utf-8") if (root / "services/data_service.py").is_file() else ""

    for route in ("/health", "/api/metrics", "/api/categories", "/api/ask"):
        if route not in app_text:
            errors.append(f"缺少路由：{route}")

    if "request.args" not in app_text:
        errors.append("未发现request.args参数处理")
    if "request.form" not in app_text:
        errors.append("未发现request.form参数处理")
    if "request.get_json" not in app_text:
        errors.append("未发现request.get_json参数处理")
    if "jsonify" not in app_text:
        errors.append("未发现jsonify响应")
    if re.search(r"TODO\s*8-[1-4]", app_text + service_text):
        errors.append("仍存在未完成的Day08 TODO")
    if "to_dict" not in service_text and "rows.append" not in service_text:
        errors.append("未发现DataFrame到普通Python数据的转换")

    test_path = root / "tests/test_app.py"
    if test_path.is_file() and count_tests(test_path) < 3:
        errors.append("Flask测试少于3条")

    readme = (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").is_file() else ""
    if "24012412" not in readme:
        errors.append("README未填写学号24012412")
    if "tests/test_app.py" not in readme:
        errors.append("README未填写测试文件")

    print(f"检查目录：{root}\n")
    for error in errors:
        print(f"[失败] {error}")
    if errors:
        print(f"\n结论：{len(errors)}项失败。")
        return 1
    print("[通过] 第8天目录、接口、序列化、README和测试检查通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
