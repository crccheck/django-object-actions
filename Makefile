VERSION = $(shell cat VERSION)
PROJECT = ./example_project
MANAGE = $(PROJECT)/manage.py

help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

quickstart: ## Set up a dev environment for the first time
quickstart: resetdb
	python $(MANAGE) createsuperuser
	python $(MANAGE) runserver

clean: ## Remove generated files
	rm -rf .coverage
	rm -rf .tox
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg
	rm -rf *.egg-info
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete

test: ## Run test suite
	python -W ignore::RuntimeWarning $(MANAGE) test django_object_actions

coverage: ## Run and then display coverage report
	coverage erase
	coverage run $(MANAGE) test django_object_actions
	coverage report --show-missing

resetdb: ## Delete and then recreate the dev sqlite database
	python $(MANAGE) reset_db --router=default --noinput
	python $(MANAGE) syncdb --noinput
	python $(MANAGE) migrate --noinput
	python $(MANAGE) loaddata sample_data

IMAGE = crccheck/django-object-actions

.PHONY: build
build: ## Build a full set of Docker images
build: build/1.9 build/1.8.7 build/1.7.11 build/1.6.11 build/1.5.12

build/%:
	docker build --build-arg DJANGO_VERSION=$* \
	  -t $(IMAGE):$$(echo "$*" | cut -f 1-2 -d.) .

run: run/1.9

run/%:
	docker run --rm -p 8000:8000 --sig-proxy=false $(IMAGE):$*

bash:
	docker run --rm -it $(IMAGE):1.9 /bin/bash

version:
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ setup.py
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ django_object_actions/__init__.py

# Release instructions
# 1. bump VERSION above
# 2. run `make release`
# 3. `git push --tags origin master`
# 4. update release notes
release: Publish a release to PyPI
release: clean version
	@git commit -am "bump version to v$(VERSION)"
	@git tag v$(VERSION)
	@-pip install wheel > /dev/null
	python setup.py sdist bdist_wheel upload
