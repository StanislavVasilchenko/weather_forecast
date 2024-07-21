FROM python:3

RUN pip install poetry

WORKDIR /code

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .


