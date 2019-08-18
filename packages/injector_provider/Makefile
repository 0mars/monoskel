.PHONY: clean tests cov docs release freeze

VERSION = $(shell pipenv run python -c "print(__import__('injector_provider').__version__)")

export PIPENV_VENV_IN_PROJECT=1

install-deps:
	pipenv install

install-dev:
	pipenv install --dev

clean:
	rm -fr docs/_build build/ dist/
	pipenv run make -C docs clean

test:
	pipenv run py.test

build:
	pipenv run mypy -m injector_provider -m tests

freeze:
	pipenv run pipenv_to_requirements -f

travis: build
	pipenv run py.test --cov

cov: test
	pipenv run coverage html
	@echo open htmlcov/index.html

apidoc:
	pipenv run make -C docs apidoc

docs:
	pipenv run make -C docs html
	@echo open docs/_build/html/index.html

release:
	@echo About to release ${VERSION}; read
	pipenv run python setup.py sdist
	pipenv run twine check dist/*
	pipenv run twine upload dist/*
	git tag -a "${VERSION}" -m "Version ${VERSION}" && git push --tags
