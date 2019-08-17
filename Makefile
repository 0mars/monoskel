# use the rest as arguments for targets
TARGET_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
# ...and turn them into do-nothing targets
$(eval $(TARGET_ARGS):;@:)

-include .env

start:
	sudo rm -rf .docker/data/zk/* && docker-compose up -d

stop:
	docker-compose stop

start-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml

rebuild:
	docker-compose build --force-rm $(TARGET_ARGS)


logs:
	docker-compose logs -f $(TARGET_ARGS)

exec:
	docker-compose exec $(TARGET_ARGS)

bash:
	docker-compose exec $(TARGET_ARGS) bash

zsh:
	docker-compose exec $(TARGET_ARGS) zsh

clean:
	docker-compose stop; docker-compose rm -svf

bootstrap:
	yarn bootstrap

run-catalog:
	yarn bootstrap && python /code/packages/catalog/src/catalog/main.py

nodemon-catalog:
	nodemon --exec make `run-catalog`

some_recipe: bootstrap
	@cd /code/packages/catalog/; python main.py && echo "success!" || { echo "failure!"; exit 0; }


restart:
	docker-compose stop $(TARGET_ARGS) && docker-compose start $(TARGET_ARGS)

clean-restart:
	docker-compose stop $(TARGET_ARGS) && docker-compose rm -f $(TARGET_ARGS) && make rebuild $(TARGET_ARGS) && docker-compose up -d
