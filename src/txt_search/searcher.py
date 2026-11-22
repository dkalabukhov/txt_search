import os
import re


def find_txt_files(folder: str, recursive: bool) -> list[str]:
    """Возвращает список полных путей ко всем .txt файлам в папке.

    Если recursive=True — обходит вложенные папки, иначе только верхний уровень.
    Недоступные папки и несуществующий путь молча пропускаются.
    """
    if not os.path.isdir(folder):
        return []

    results: list[str] = []

    if recursive:
        for root, _dirs, files in os.walk(folder):
            for name in files:
                if name.lower().endswith(".txt"):
                    results.append(os.path.join(root, name))
    else:
        try:
            entries = os.listdir(folder)
        except OSError:
            return []

        for name in entries:
            if not name.lower().endswith(".txt"):
                continue
            full = os.path.join(folder, name)
            if os.path.isfile(full):
                results.append(full)

    return results


def _read_text(path: str) -> str | None:
    """Читает файл, пытаясь определить кодировку.

    Сначала UTF-8, при неудаче — Windows-1251.
    Возвращает None, если файл прочитать не удалось.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        pass
    except OSError:
        return None

    try:
        with open(path, "r", encoding="cp1251") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return None


def search_in_files(
    files: list[str], word: str, case_sensitive: bool
) -> list[tuple[str, int, str]]:
    """Ищет слово (как целое) в файлах.

    Возвращает список кортежей (путь, номер_строки, текст_строки).
    Пустое слово даёт пустой результат.
    """
    if not word:
        return []

    flags = 0 if case_sensitive else re.IGNORECASE
    pattern = re.compile(rf"\b{re.escape(word)}\b", flags)

    results: list[tuple[str, int, str]] = []

    for path in files:
        content = _read_text(path)
        if content is None:
            continue

        for line_no, line in enumerate(content.splitlines(), start=1):
            if pattern.search(line):
                results.append((path, line_no, line))

    return results