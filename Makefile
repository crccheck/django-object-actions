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
	PYTHONPATH=. python $(MANAGE) runserver

clean: ## Remove generated files
	rm -rf .coverage
	rm -rf build
	rm -rf dist
	rm -rf *.egg
	rm -rf *.egg-info
	find . -name ".DS_Store" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} \; || true

install: ## Install development dependencies
	poetry install
	pip install Django

lint: ## Check the project for lint errors
	poetry run ruff check .
	poetry run ruff format --diff .

tdd: ## Run tests with a file watcher
	PYTHONPATH=. nodemon --ext py -x sh -c "poetry run python -W ignore::RuntimeWarning $(MANAGE) test --failfast django_object_actions || true"

test: ## Run test suite
	PYTHONPATH=. poetry run python -W ignore::RuntimeWarning $(MANAGE) test django_object_actions

coverage: ## Run and then display coverage report
	poetry run coverage erase
	PYTHONPATH=. poetry run coverage run $(MANAGE) test django_object_actions
	poetry run coverage report --show-missing

resetdb: ## Delete and then recreate the dev sqlite database
	python $(MANAGE) reset_db --router=default --noinput
	python $(MANAGE) migrate --noinput
	python $(MANAGE) loaddata sample_data

# DEPRECATED: Docker builds are currently broken and will likely get deleted rather than fixed

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
