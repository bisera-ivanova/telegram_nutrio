FROM python:3.10-slim-buster

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD [ "python", "main.py" ]

