FROM python:3.11-alpine

# Install dev tools for me
RUN apk add --no-cache vim bash git

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./src/ ./src

CMD [ "python3", "src/app.py" ]
