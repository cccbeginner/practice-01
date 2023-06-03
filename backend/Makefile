run:
	poetry run uvicorn main:app --reload
install:
	sudo apt install python3 python3-poetry libpq-dev
	poetry install
	poetry run alembic upgrade head