FROM python:2.7
MAINTAINER Matt Berther

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 5000

CMD [ "python", "app.py" ]
