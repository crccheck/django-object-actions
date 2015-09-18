VERSION=0.5.1
PROJECT=./example_project
MANAGE=$(PROJECT)/manage.py

help:
	@echo "make commands:"
	@echo "  make help       - this help"
	@echo "  make quickstart - setup a dev environment the first time"
	@echo "  make clean      - remove generated files"
	@echo "  make test       - run test suite"
	@echo "  make coverage   - get coverage report"
	@echo "  make resetdb    - delete and recreate the sqlite database"
	@echo "  make release    - publish a release to PyPI"

# just a demo of how to get up and running quickly
quickstart: resetdb
	python $(MANAGE) createsuperuser
	python $(MANAGE) runserver

clean:
	rm -rf .coverage
	rm -rf .tox
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg
	rm -rf *.egg-info
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete

test:
	python -W ignore::RuntimeWarning $(MANAGE) test django_object_actions

coverage:
	coverage erase
	coverage run $(MANAGE) test django_object_actions
	coverage report --show-missing

# destroy and then recreate your database
resetdb:
	python $(MANAGE) reset_db --router=default --noinput
	python $(MANAGE) syncdb --noinput
	python $(MANAGE) migrate --noinput
	python $(MANAGE) loaddata sample_data

# Set the version. Done this way to avoid fancy, brittle Python import magic
version:
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ setup.py
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ django_object_actions/__init__.py

# Release instructions
# 1. bump VERSION above
# 2. run `make release`
# 3. `git push --tags origin master`
# 4. update release notes
release: clean version
	@git commit -am "bump version to v$(VERSION)"
	@git tag v$(VERSION)
	@-pip install wheel > /dev/null
	python setup.py sdist bdist_wheel upload
