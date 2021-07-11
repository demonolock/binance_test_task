FROM python:3.8-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update -qy && \
    apt-get install -y libpq-dev gcc

RUN pip install poetry==1.*
RUN pip install binance

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

COPY ./binance_test_task  /code/binance_test_task/
COPY ./$STATIC_FOLDER  /code/$STATIC_FOLDER/

RUN poetry install --no-dev --no-interaction --no-ansi

ENTRYPOINT ["python3", "/code/binance_test_task/__init__.py"]