prepare :
	pyenv local $(pyenv local)
	virtualenv -p $(which python) venv
	source venv/bin/activate
	pip install -r requirements.txt

start :
	source venv/bin/activate

test :
	python -m pytest -vv -s

style :
	pycodestyle . --max-line-length=119 --exclude venv
