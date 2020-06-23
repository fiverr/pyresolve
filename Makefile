prepare :
	pyenv local $(pyenv local)
	virtualenv -p $(which python) venv
	source venv/bin/activate
	pip install -r requirements.txt

start :
	source venv/bin/activate

build :
	# pip install setuptools wheel
	python setup.py sdist bdist_wheel

upload :
	# pip install twine
	python -m twine upload dist/*

test :
	python -m pytest -vv -s

style :
	pycodestyle . --max-line-length=119 --exclude venv
