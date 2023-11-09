FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

# Install the requirements specified in file using RUN
RUN pip3 install -r requirements.txt

# copy all items in current local directory (source) to current container directory (destination)
COPY ./src/ ./src

# command to run when image is executed inside a container
CMD [ "python3", "src/app.py" ]