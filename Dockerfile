FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /myapp

ADD . /myapp

WORKDIR /myapp
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
