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

lint: ## Check code style
	black --check .

coverage: ## Run and then display coverage report
	coverage erase
	coverage run $(MANAGE) test django_object_actions
	coverage report --show-missing

resetdb: ## Delete and then recreate the dev sqlite database
	python $(MANAGE) reset_db --router=default --noinput
	python $(MANAGE) migrate --noinput
	python $(MANAGE) loaddata sample_data

docker/build: ## Build a full set of Docker images
docker/build: docker/build/3.1 docker/build/3.0 docker/build/2.2.6 docker/build/2.1.13 docker/build/2.0.13 docker/build/1.11.25 docker/build/1.10.8 docker/build/1.9.13 docker/build/1.8.18

docker/build/%:
	docker build --build-arg DJANGO_VERSION=$* \
	  -t $(IMAGE):$$(echo "$*" | cut -f 1-2 -d.) .

run: run/3.1

run/%:
	docker run --rm -p 8000:8000 -it $(IMAGE):$*

docker/publish: ## Publish Docker images to the hub
	docker push $(IMAGE):3.1
	docker push $(IMAGE):3.0
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
	docker run --rm -it $(IMAGE):3.1 /bin/sh

.PHONY: version
version:
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ setup.py
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ django_object_actions/__init__.py
	# TODO figure out how to get Make to insert a \n
	git add . && standard-version --commit-all  --changelogHeader "# Changelog"

# Release instructions
# 1. bump VERSION
# 2. `make version`
# 3. `make release`
# 4. `git push --follow-tags origin master`
# 5. `chandler push`
# 6. `make docker/build docker/publish`
release: clean
	@-pip install twine wheel > /dev/null
	python setup.py sdist bdist_wheel
	twine upload dist/*
