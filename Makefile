PROJECT=./example_project

help:
	@echo "  make test    - run test suite"
	@echo "  make resetdb - delete and recreate the sqlite database"


test:
#
#   -s    don't capture stdout
#
	python $(PROJECT)/manage.py test -s


resetdb:
	$(foreach db, $(wildcard $(PROJECT)/*.sqlite),\
		rm $(db);)
	python $(PROJECT)/manage.py syncdb --noinput


.PHONY: test resetdb
