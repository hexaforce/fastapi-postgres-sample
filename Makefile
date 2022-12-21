
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
