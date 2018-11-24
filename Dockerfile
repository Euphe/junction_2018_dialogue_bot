FROM python:3.7-slim
WORKDIR /src

RUN apt update && apt install bash

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /src
RUN python setup.py develop

EXPOSE 80
