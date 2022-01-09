FROM python:3.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем директорию для приложения
RUN mkdir /app
COPY . /app
# COPY ./requirements.txt /app/requirements.txt

# Устанавливаем необходимое для psycopg2, обновляем pip, устанавливаем зависимости
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN pip install --upgrade pip && pip install -r app/requirements.txt

WORKDIR /app

# RUN apk add --update --no-cache postgresql-client jpeg-dev

# FROM ubuntu

# RUN apt update && apt install -y cowsay && ln /usr/games/cowsay /usr/bin/cowsay

# ENTRYPOINT ["cowsay"]
