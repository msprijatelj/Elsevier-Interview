all: install deploy

install:
	python3 -m venv .venv
	.venv/bin/pip3 install -r api-challenge/requirements.txt

deploy:
	cd api-challenge; python3 safe_harbor.py

uninstall:
	pip freeze | xargs pip uninstall -y