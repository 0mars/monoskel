# use the rest as arguments for targets
TARGET_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
# ...and turn them into do-nothing targets
$(eval $(TARGET_ARGS):;@:)

# container
start:
	docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose stop $(TARGET_ARGS) && docker-compose start $(TARGET_ARGS)

rebuild:
	docker-compose build --force-rm $(TARGET_ARGS)

clean-restart:
	docker-compose stop $(TARGET_ARGS) && docker-compose rm -f $(TARGET_ARGS) && make rebuild $(TARGET_ARGS) && docker-compose up -d

bash:
	docker-compose exec $(TARGET_ARGS) zsh

logs:
	docker-compose logs -f $(TARGET_ARGS)


# app
freeze:
	pipenv run pipenv_to_requirements -f


install:
	pip install -r requirements-dev.txt

run:
	@cd src; gunicorn -b 0.0.0.0:8000 product_manager.configurations.app.main:app -w 1 -k gevent --reload && echo "success!" || { echo "Crashed!"; exit 0; }

test:
	python manage.py test

watch:
	eval watchexec -r -e 'py' -i './product_manager' "docker-compose up"
