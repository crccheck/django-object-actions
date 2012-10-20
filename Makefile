PROJECT=./example_project

help:
	@echo "  make test    - run test suite"
	@echo "  make resetdb - delete and recreate the sqlite database"


test:
	python $(PROJECT)/manage.py test


resetdb:
	$(foreach db, $(wildcard $(PROJECT)/*.sqlite),\
		rm $(db);)
	python $(PROJECT)/manage.py syncdb --noinput


.PHONY: test resetdb
