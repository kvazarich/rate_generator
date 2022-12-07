include ./.env

SHELL := /bin/bash
PYTHON := python
OS_RELEASE = $(lsb_release -cs)
DOCKER_COMPOSE := ./docker-compose.local.yml

help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# =================================================================================================
# FastAPI
# =================================================================================================

.PHONY: run-local
run-local:
	uvicorn main:app --reload

# =================================================================================================
# Alembic
# =================================================================================================

.PHONY: migrations
migrations: ## Run alembic revision for create migrations
	alembic revision --autogenerate

.PHONY: migrate
migrate: ## Run alembic upgrade
	alembic upgrade head

.PHONY: migrate_rollback
migrate_rollback: ## Run alembic upgrade
	alembic downgrade -1