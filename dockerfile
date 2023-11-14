FROM python:3.11-buster

# Install dev tools for me
RUN apt-get update && apt-get install -y vim bash

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./src/ ./src

CMD [ "python3", "src/app.py" ]
