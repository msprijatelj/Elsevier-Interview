

install:
	cd api-challenge/
	pip install -r requirements.txt

uninstall:
	pip freeze | xargs pip uninstall -y