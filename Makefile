VERSION = $(shell cat VERSION)
PROJECT = ./example_project
MANAGE = $(PROJECT)/manage.py
IMAGE = crccheck/django-object-actions

help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

quickstart: ## Set up a dev environment for the first time
quickstart: resetdb
	python $(MANAGE) createsuperuser
	python $(MANAGE) runserver

dev: ## Run the example project
	@echo Browse at http://localhost:8000/admin/
	python $(MANAGE) runserver

clean: ## Remove generated files
	rm -rf .coverage
	rm -rf .tox
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg
	rm -rf *.egg-info
	find . -name ".DS_Store" -delete
	find . -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} \; || true

install: ## Install development requirements
	@[ -n "${VIRTUAL_ENV}" ] || (echo "ERROR: This should be run from a virtualenv" && exit 1)
	pip install -r requirements.txt
	pip install Django tox

.PHONY: requirements.txt
requirements.txt: ## Regenerate requirements.txt
	pip-compile requirements.in > $@

tdd: ## Run tests with a file watcher
	nodemon --ext py -x sh -c "python -W ignore::RuntimeWarning $(MANAGE) test --failfast django_object_actions || true"

test: ## Run test suite
	python -W ignore::RuntimeWarning $(MANAGE) test django_object_actions

coverage: ## Run and then display coverage report
	coverage erase
	coverage run $(MANAGE) test django_object_actions
	coverage report --show-missing

resetdb: ## Delete and then recreate the dev sqlite database
	python $(MANAGE) reset_db --router=default --noinput
	python $(MANAGE) migrate --noinput
	python $(MANAGE) loaddata sample_data

.PHONY: build
build: ## Build a full set of Docker images
build: build/2.2.6 build/2.1.13 build/2.0.13 build/1.11.25 build/1.10.8 build/1.9.13 build/1.8.18

build/%:
	docker build --build-arg DJANGO_VERSION=$* \
	  -t $(IMAGE):$$(echo "$*" | cut -f 1-2 -d.) .

run: run/2.2

run/%:
	docker run --rm -p 8000:8000 -it $(IMAGE):$*

docker/publish: ## Publish Docker images to the hub
	docker push $(IMAGE):2.2
	docker push $(IMAGE):2.1
	docker push $(IMAGE):2.0
	docker push $(IMAGE):1.11
	docker push $(IMAGE):1.10
	docker push $(IMAGE):1.9
	docker push $(IMAGE):1.8

test/%:
	docker run --rm -p 8000:8000 -t $(IMAGE):$* make test

bash:
	docker run --rm -it $(IMAGE):2.2 /bin/sh

.PHONY: version
version:
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ setup.py
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ django_object_actions/__init__.py

# Release instructions
# 1. update CHANGELOG
# 2. bump VERSION
# 3. run `make release`
# 4. `git push --tags origin master`
# 5. update release notes
# 6. `chandler push`
# 6. `make build docker/publish`
release: clean version
	@git commit -am "bump version to v$(VERSION)"
	@git tag v$(VERSION)
	@-pip install wheel > /dev/null
	python setup.py sdist bdist_wheel upload
