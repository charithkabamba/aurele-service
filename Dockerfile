FROM python:3.11-slim

ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN python -m venv venv

ENV PATH="/env/bin/:$PATH"

COPY entrypoint.sh /app/entrypoint.sh

# ajouter fichier shell

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

