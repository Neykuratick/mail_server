format:
	black --line-length 100 .
run:
	uvicorn main:app --reload