install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8

tests:
	poetry run pytest

