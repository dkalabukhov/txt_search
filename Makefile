lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

run:
	uv run python -m txt_search.main

.PHONY: lint run lint-fix