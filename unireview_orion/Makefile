run:
	export $$(cat .env | xargs) && python manage.py runserver

prod:
	export $$(cat .env.production | xargs) && ./api/runner.sh
