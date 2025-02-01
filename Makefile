.PHONY: venv install upgrade clean run

venv:
	python -m venv venv
	./venv/bin/pip install --upgrade pip

install: venv
	./venv/bin/pip install -r requirements.txt

upgrade:
	./venv/bin/pip install --upgrade pip

clean:
	rm -rf __pycache__ *.pyc *.pyo venv

run: install
	./venv/bin/python main.py