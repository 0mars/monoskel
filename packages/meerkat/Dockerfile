FROM python:3.9.1-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y automake build-essential libffi-dev libssl-dev nodejs npm protobuf-compiler git zsh postgresql util-linux && \
    rm -f /tmp/*

RUN sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

RUN npm config set unsafe-perm true

RUN npm i -g nodemon yarn
RUN pip install --upgrade pip pipenv

# set working directory
RUN mkdir -p /code/packages/meerkat
WORKDIR /code/packages/meerkat

# add requirements
COPY ./requirements-dev.txt /code/packages/meerkat/requirements-dev.txt
COPY ./requirements.txt /code/packages/meerkat/requirements.txt

# install requirements
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

# add entrypoint.sh
COPY ./.docker/entrypoint.sh /code/packages/meerkat/.docker/entrypoint.sh

EXPOSE 8000

# run server
CMD ["sh", "/code/packages/meerkat/.docker/entrypoint.sh"]
