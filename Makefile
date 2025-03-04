up:
	docker compose up -d --build

down:
	docker compose down --remove-orphans  --rmi local --volumes
