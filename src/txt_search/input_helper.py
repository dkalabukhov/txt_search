import os
from typing import Any

from InquirerPy.resolver import prompt
from InquirerPy.validator import PathValidator


def ask_folder() -> str | None:
    error_msg = (
        "Убедитесь, что путь не содержит лишних кавычек"
        " и является директорией"
    )
    questions: list[dict[str, Any]] = [
        {
            "type": "filepath",
            "message": "Выберите папку:",
            "validate": PathValidator(is_dir=True, message=error_msg),
            "only_directories": True,
        }
    ]

    try:
        result = prompt(questions)
        folder = result[0]
    except KeyboardInterrupt:
        return None

    if isinstance(folder, str):
        return folder

    return None


def ask_recursive() -> bool | None:
    questions: list[dict[str, Any]] = [
        {
            "type": "confirm",
            "message": "Искать во вложенных папках?",
            "default": True,   # Enter = да
        }
    ]
    try:
        result = prompt(questions)
        value = result[0]
    except KeyboardInterrupt:
        return None

    if isinstance(value, bool):
        return value

    return None


def ask_word() -> str | None:
    questions = [
        {
            "type": "input",
            "message": "Поисковое слово:",
        }
    ]

    try:
        result = prompt(questions)
        word = result[0]
    except KeyboardInterrupt:
        return None

    if isinstance(word, str):
        return word.strip()

    return None


def ask_case_sensitive() -> bool | None:
    questions: list[dict[str, Any]] = [
        {
            "type": "confirm",
            "message": "Учитывать регистр при поиске?",
            "default": False,
        }
    ]
    try:
        result = prompt(questions)
        value = result[0]
    except KeyboardInterrupt:
        return None

    if isinstance(value, bool):
        return value

    return None


def normalize_path(raw: str) -> str:
    p = raw.strip()
    if len(p) >= 2 and p[0] == p[-1] and p[0] in ('"', "'", '“', '”'):
        p = p[1:-1].strip()
    return os.path.expanduser(p)


def validate_folder(path: str) -> bool:
    return os.path.isdir(normalize_path(path))