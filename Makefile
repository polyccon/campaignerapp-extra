COMPOSE_PROJECT_NAME     ?= ${CI_PROJECT_NAME}${CI_PIPELINE_ID}
PREFIX_COMPOSE           := \
	COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME} \
	${CI_COMPOSE_PREFIX} \
	docker-compose ${CI_COMPOSE_ARGS}
RUN_COMPOSE				 := ${PREFIX_COMPOSE} run --rm backend

sh: ## Follow the logs for the microservice
	${RUN_COMPOSE} /bin/bash

manage:
	${RUN_COMPOSE} python manage.py ${MANAGE_CMD}

migrations: ## Make migrations in the local source against the built docker db from previous state
	${RUN_COMPOSE} python manage.py makemigrations

migrate:
	${RUN_COMPOSE} python manage.py migrate

shell_plus:
	${RUN_COMPOSE} python manage.py shell_plus