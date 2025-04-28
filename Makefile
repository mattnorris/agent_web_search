CODE = src
REQUIREMENTS = requirements.txt

# Export the requirements with no environment markers.
$(REQUIREMENTS):
	@poetry export --without-hashes -f $(REQUIREMENTS) --output $(REQUIREMENTS)
	@sed -i '' 's/;.*//' $(REQUIREMENTS)

# Lint code with pylint and perflint, for performance.
lint:
	@poetry run pylint $(CODE) --load-plugins perflint

# Lint code with ruff to check for unused imports, etc.
ruff:
	@poetry run ruff check $(CODE)


.PHONY: lint ruff