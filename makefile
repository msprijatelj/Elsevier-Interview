all: install deploy

install:
	cd api-challenge; pip install -r requirements.txt

deploy:
	cd api-challenge; python3 safe_harbor.py

uninstall:
	pip freeze | xargs pip uninstall -y