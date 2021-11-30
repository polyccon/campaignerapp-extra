FROM python:alpine as base

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5500
