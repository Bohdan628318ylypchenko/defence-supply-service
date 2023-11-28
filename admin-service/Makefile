install:
	pip install -r requirements.txt

unit_test:
	coverage run -m pytest test/unit

coverage:
	coverage report -m --omit="*router.py","*error_handler.py","*conftest.py","test/*"
