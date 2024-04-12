FROM python:3.8.13-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /api

RUN pip install django 
RUN pip install django-cors-headers --user

COPY . .

EXPOSE 8000