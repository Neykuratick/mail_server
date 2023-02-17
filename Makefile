format:
	black --line-length 100 .
run:
	uvicorn main:app --reload
migrations:
	alembic revision --autogenerate -m "$(m)"
migrate:
	alembic upgrade head