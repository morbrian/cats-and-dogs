FROM python:3.9.15-slim

COPY requirements/common.txt requirements/common.txt
RUN pip install -U pip && pip install -r requirements/common.txt

COPY ./apis /app/apis
COPY ./bin /app/bin
COPY ./app.py /app
COPY ./wsgi.py /app
WORKDIR /app

RUN useradd demo
USER demo

EXPOSE 8080

ENTRYPOINT ["bash", "/app/bin/run.sh"]
