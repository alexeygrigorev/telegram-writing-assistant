.PHONY: run tests tests_integration

# Run the Telegram bot
run:
	uv run python main.py

# Run all tests
tests:
	uv run pytest tests/ -v

# Run integration tests only
tests_integration:
	uv run pytest tests_integration/ -v
