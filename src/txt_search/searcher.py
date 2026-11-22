def find_txt_files(folder: str, recursive: bool) -> list[str]:
    raise NotImplementedError


def search_in_files(
    files: list[str], word: str, case_sensitive: bool
) -> list[tuple[str, int, str]]:
    raise NotImplementedError