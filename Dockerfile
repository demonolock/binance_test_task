FROM python:3.8-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update -qy && \
    apt-get install -y libpq-dev gcc

RUN pip install binance
RUN pip install python-binance
RUN pip install pydantic

WORKDIR /code
COPY app  /code/app
ENV PYTHONPATH /code

ENTRYPOINT ["python3", "/code/app/__init__.py"]
