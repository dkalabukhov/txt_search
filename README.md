# txt-search

A simple console utility to search for a word in `.txt` files inside a chosen folder.

## Features

- Search for a whole word (not a substring) in `.txt` files
- Optional recursive search through subfolders
- Optional case-sensitive search (case-insensitive by default)
- Handles UTF-8 and Windows-1251 encoded files
- Skips unreadable files instead of crashing
- Results are printed in the familiar `path:line: text` format

## Requirements

- Python 3.15 or newer

## Installation

Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd txt-search
uv sync
```

## Usage

Run the utility from the project root:

```bash
uv run python -m txt_search.main
```

The program will interactively ask for:

1. Folder — path to the folder to search in (supports ~ for the home directory and quoted paths)

2. Word — the word to search for

3. Recursive — whether to search inside subfolders (default: yes)

4. Case-sensitive — whether to match case exactly (default: no)

## Example
Введите путь к папке: ~/Desktop/test
Поисковое слово: report
Искать во вложенных папках? (Y/n): y
Учитывать регистр при поиске? (y/N): n

Проверяю 12 файл(ов)...

Найдено совпадений: 3

C:\Users\user\Desktop\test\2024\january.txt:14: monthly report is ready
C:\Users\user\Desktop\test\2024\february.txt:7: Report approved
C:\Users\user\Desktop\test\archive\old.txt:42: the report was lost

If nothing matches, the program prints Ничего не найдено. If the folder contains
no .txt files at all, it prints В папке нет .txt файлов. — so you can tell the
difference between "no files to search" and "word not found".

## Testing

Run the following command from the project root:

```bash
uv run pytest -v
```

## Building an .exe

Run the following command from the project root:

```bash
uv run pyinstaller --onefile --paths=./src --copy-metadata readchar src/txt_search/main.py
```