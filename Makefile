test:
	python -m pytest -vv -s
	pycodestyle . --max-line-length=119 --exclude venv
