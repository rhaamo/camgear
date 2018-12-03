# vim:set ft=dockerfile:
FROM python:3.7-alpine

LABEL maintainer="Dashie <dashie@sigpipe.me>"

LABEL org.label-schema.license=MIT \
    org.label-schema.name=reel2bits-web \
    org.label-schema.vcs-url=https://github.com/rhaamo/camgear \
    org.label-schema.build-date=$DRONE_BUILD_STARTED \
    org.label-schema.vcs-ref=$DRONE_COMMIT_SHA

RUN mkdir -p /app /data /config
WORKDIR /app

ADD requirements.txt /app/
RUN apk add --no-cache git git libffi postgresql-client
RUN apk add --no-cache --virtual .build-deps gcc g++ libffi-dev postgresql-dev cmake make pkgconfig jpeg-dev zlib-dev python-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir waitress
RUN apk del .build-deps

ADD . /app/
ADD entrypoint.sh /
ADD config.py.sample /config/config.py

VOLUME ["/data", "/config"]

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["waitress-serve", "--call", "app:create_app", "--host", "0.0.0.0", "--port", "8000"]
