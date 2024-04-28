# Target to run the main Python script
# If the main.py doesnt exist, it wont run it.
run: main.py
	poetry run python main.py


# Target to clean up Python bytecode files
clean:
	rm -f *.pyc __pycache__/*.pyc

# Phony target for 'help' to avoid issues
.PHONY: help

# Help message
help:
	@echo "Available targets:"
	@echo "  run     - Run the main Python script (main.py)"
	@echo "  clean   - Clean up Python bytecode files"
	@echo "  help    - Show this help message"