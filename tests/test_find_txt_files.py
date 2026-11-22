import os
from pathlib import Path

from txt_search.searcher import find_txt_files


def _names(paths: list[str]) -> set[str]:
    """Возвращает множество имён файлов (без каталогов) для сравнения."""
    return {os.path.basename(p) for p in paths}


def test_finds_only_txt(sample_tree: Path):
    result = find_txt_files(str(sample_tree), recursive=False)
    assert _names(result) == {"root.txt", "notes.TXT", "empty.txt"}


def test_txt_extension_case_insensitive(sample_tree: Path):
    result = find_txt_files(str(sample_tree), recursive=False)
    assert "notes.TXT" in _names(result)


def test_recursive_finds_nested(sample_tree: Path):
    result = find_txt_files(str(sample_tree), recursive=True)
    names = _names(result)
    assert "root.txt" in names
    assert "nested.txt" in names
    assert "deep.txt" in names


def test_non_recursive_ignores_subfolders(sample_tree: Path):
    result = find_txt_files(str(sample_tree), recursive=False)
    names = _names(result)
    assert "nested.txt" not in names
    assert "deep.txt" not in names


def test_empty_folder(tmp_path: Path):
    result = find_txt_files(str(tmp_path), recursive=False)
    assert result == []


def test_returns_full_paths(sample_tree: Path):
    result = find_txt_files(str(sample_tree), recursive=True)
    assert result, "должен быть хотя бы один файл"
    for p in result:
        assert os.path.isabs(p)
        assert p.lower().endswith(".txt")


def test_nonexistent_folder(tmp_path: Path):
    missing = tmp_path / "no_such_dir"
    result = find_txt_files(str(missing), recursive=False)
    assert result == []