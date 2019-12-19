test:
	pytest -v
run:
	FLASK_ENV=development FLASK_APP=app:"create_app('dev')" flask run