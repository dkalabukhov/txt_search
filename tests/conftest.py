from pathlib import Path

import pytest


@pytest.fixture
def sample_tree(tmp_path: Path) -> Path:
    """Строит дерево файлов для тестов и возвращает корень."""
    (tmp_path / "root.txt").write_text(
        "первая строка\nздесь кот\nтретья\n",
        encoding="utf-8"
    )
    (tmp_path / "notes.TXT").write_text("Кот спит\n", encoding="utf-8")
    (tmp_path / "other.log").write_text("кот в логе\n", encoding="utf-8")
    (tmp_path / "empty.txt").write_text("", encoding="utf-8")

    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "nested.txt").write_text(
        "который час\nкот и пёс\n",
        encoding="utf-8"
    )

    deep = sub / "deep"
    deep.mkdir()
    (deep / "deep.txt").write_text("кота позвали\n", encoding="utf-8")

    return tmp_path


@pytest.fixture
def cp1251_file(tmp_path: Path) -> Path:
    """Файл в кодировке Windows-1251 с кириллицей."""
    path = tmp_path / "win.txt"
    path.write_bytes("Привет кот\n".encode("cp1251"))
    return path