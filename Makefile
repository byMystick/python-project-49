install: 				# Install dependencies
	poetry install
brain-games: 				# Run project
	poetry run brain-games
build:					# Packaging
	poetry build
publish:				# Debug publishing
	poetry publish --dry-run
package-install:			# Install package
	python3 -m pip install --user dist/*.whl
lint:				# Сode style test
	poetry run flake8 brain_games
