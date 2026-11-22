from txt_search.input_helper import (
    ask_case_sensitive,
    ask_folder,
    ask_recursive,
    ask_word,
    normalize_path,
    validate_folder,
)
from txt_search.searcher import find_txt_files, search_in_files


def print_results(results: list[tuple[str, int, str]]) -> None:
    """Печатает результаты в формате путь:строка: текст."""
    if not results:
        print("Ничего не найдено.")
        return

    print(f"\nНайдено совпадений: {len(results)}\n")
    for path, line_no, line in results:
        print(f"{path}:{line_no}: {line}")


def main() -> None:
    folder = ask_folder()
    if not folder:
        print("Папка не выбрана")
        return
    if not validate_folder(folder):
        print(f"{folder} не является директорией")
        return

    normalized_folder = normalize_path(folder)

    word = ask_word()
    if not word:
        print("Слово не задано")
        return

    recursive = ask_recursive()
    if recursive is None:
        print("Поиск отменён")
        return

    case_sensitive = ask_case_sensitive()
    if case_sensitive is None:
        print("Поиск отменён")
        return

    files = find_txt_files(normalized_folder, recursive)
    if not files:
        print("В папке нет .txt файлов.")
        return

    print(f"\nПроверяю {len(files)} файл(ов)...")
    results = search_in_files(files, word, case_sensitive)
    print_results(results)


if __name__ == "__main__":
    try:
        main()
    finally:
        input('\nНажмите Enter, чтобы завершить программу...')