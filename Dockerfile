FROM python:3.11-slim

ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app

WORKDIR /app

RUN python -m venv venv

ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/

COPY entrypoint.sh /app/entrypoint.sh

# ajouter fichier shell

