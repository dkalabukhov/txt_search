from txt_search.input_helper import (
    ask_folder,
    ask_recursive,
    ask_word,
    validate_folder,
)


def main() -> None:
    folder = ask_folder()
    if not folder:
        print('Папка не выбрана')
        return
    if not validate_folder(folder):
        print(f'{folder} не является директорией')
        return

    recursive = ask_recursive()
    if recursive is None:
        print('Поиск отменён')
        return

    word = ask_word()
    if not word:
        print('Слово не задано')
        return

    scope = 'с вложенными папками' if recursive else 'только в выбранной папке'
    print(f"Ищу '{word}' в '{folder}' ({scope})")


if __name__ == '__main__':
    main()