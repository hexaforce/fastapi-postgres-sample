
upf:
	docker compose up --build

up:
	docker compose up -d --build

log:
	docker compose logs -f

down:
	docker compose down

del:
	docker system prune -a --volumes

test:
	docker compose exec -T api pytest ./app/tests

revision:
	docker compose exec -T -w / api alembic -x target=main revision --autogenerate

model:
	sqlacodegen postgresql://postgres:password@localhost/example > app/db/model.py

isort:
	isort --force-single-line-imports app/

autoflake:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app/ --exclude=__init__.py

black:
	black --check --verbose --exclude="model.py" app/

flake8:
	flake8 app/
