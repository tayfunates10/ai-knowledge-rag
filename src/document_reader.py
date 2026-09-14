from pathlib import Path


def read_document(file_path: str) -> str:
    path = path(file_path)
    content = path.read_text(encoding="utf-8")
    return content
