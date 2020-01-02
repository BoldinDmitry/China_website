# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/ChinaBack

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install Pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/ChinaBack/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/ChinaBack/entrypoint.sh

# copy media folder
COPY ./media /usr/src/ChinaBack/media

# copy project
COPY . /usr/src/ChinaBack/

# create the appropriate directories

ENTRYPOINT ["/usr/src/ChinaBack/entrypoint.sh"]
