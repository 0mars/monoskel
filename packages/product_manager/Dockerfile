FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache make build-base libffi-dev libressl-dev nodejs npm protobuf git zsh postgresql-dev util-linux && \
    rm -f /tmp/* /etc/apk/cache/*

RUN sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

RUN npm i -g nodemon yarn
RUN pip install --upgrade pip pipenv

# set working directory
RUN mkdir -p /code/packages/product_manager
WORKDIR /code/packages/product_manager

# add requirements
COPY ./requirements-dev.txt /code/packages/product_manager/requirements-dev.txt
COPY ./requirements.txt /code/packages/product_manager/requirements.txt

# install requirements
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

# add entrypoint.sh
COPY ./.docker/entrypoint.sh /code/packages/product_manager/.docker/entrypoint.sh

EXPOSE 8000

# run server
CMD ["sh", "/code/packages/product_manager/.docker/entrypoint.sh"]
