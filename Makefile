lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

run:
	uv run python -m txt_search.main

test:
	uv run pytest -v

build:
	uv run pyinstaller --onefile --paths=./src --copy-metadata readchar src/txt_search/main.py

.PHONY: lint run lint-fix test build