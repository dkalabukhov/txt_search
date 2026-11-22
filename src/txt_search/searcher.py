import os


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


def search_in_files(
    files: list[str], word: str, case_sensitive: bool
) -> list[tuple[str, int, str]]:
    raise NotImplementedError