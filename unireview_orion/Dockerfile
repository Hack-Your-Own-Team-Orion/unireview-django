FROM python:3-alpine

ADD . /api
WORKDIR /api

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN pip install uwsgi
RUN pip install -r requirements.txt

CMD ["./api/runner.sh"]
