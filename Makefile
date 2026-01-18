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
	pip install -e '.[build,dev]'
	pip install Django

lint: ## Check the project for lint errors
	ruff check .
	ruff format --diff .

tdd: ## Run tests with a file watcher
	PYTHONPATH=. nodemon --ext py -x sh -c "python -W ignore::RuntimeWarning $(MANAGE) test --failfast django_object_actions || true"

test: ## Run test suite
	PYTHONPATH=. python -W ignore::RuntimeWarning $(MANAGE) test django_object_actions

coverage: ## Run and then display coverage report
	coverage erase
	PYTHONPATH=. coverage run $(MANAGE) test django_object_actions
	coverage report --show-missing

resetdb: ## Delete and then recreate the dev sqlite database
	python $(MANAGE) reset_db --router=default --noinput
	python $(MANAGE) migrate --noinput
	python $(MANAGE) loaddata sample_data

docker/build: ## Build Docker image
	docker build -t $(IMAGE):latest .

docker/run: ## Run Docker image
	@echo Login at http://localhost:8000/admin/ with admin/admin
	docker run --rm -p 8000:8000 -it $(IMAGE):latest

docker/test: ## Run tests in Docker
	docker run --rm -t $(IMAGE):latest make test
