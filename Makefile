COMPOSE_PROJECT_NAME     ?= ${CI_PROJECT_NAME}${CI_PIPELINE_ID}
PREFIX_COMPOSE           := \
	COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME} \
	${CI_COMPOSE_PREFIX} \
	docker-compose ${CI_COMPOSE_ARGS}
RUN_COMPOSE				 := ${PREFIX_COMPOSE} run --rm backend

help: ## Prints this help/overview message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-17s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

stop: ## Stops all containers
	${PREFIX_COMPOSE} stop

run: stop build up ## Builds all containers and (re)runs them in foreground.

restart: stop start ## Restarts all containers

build: ## Builds all containers
	${PREFIX_COMPOSE} build

build_no_cache: ## Builds all containers without cache
	${PREFIX_COMPOSE} build --no-cache

rebuild: down build start ## Fully rebuild containers

up: ## Starts all containers in foreground
	${PREFIX_COMPOSE} up

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