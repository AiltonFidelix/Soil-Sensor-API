FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update \
    && apt-get install -y sqlite3

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "--bind" , "0.0.0.0:5000", "setup.wsgi"]