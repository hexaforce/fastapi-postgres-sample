
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

