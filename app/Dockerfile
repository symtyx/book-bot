FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="Patrick Cockrill pcockrill2@gmail.com"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /app

ADD . /app
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 8000

CMD ["python3" "app.py"]