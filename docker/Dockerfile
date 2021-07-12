FROM python:3.8-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update -qy && \
    apt-get install -y libpq-dev gcc

RUN pip install binance
RUN pip install python-binance

WORKDIR /code

COPY ./binance_test_task  /code/binance_test_task/

CMD ["/code/binance_test_task/test.py"]

ENTRYPOINT ["python3", "/code/binance_test_task/__init__.py"]
