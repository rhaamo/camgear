FROM alpine:3.10

ADD ./ /app/

RUN \
    echo 'installing dependencies' && \
    apk add --no-cache \
    bash \
    git \
    musl-dev \
    gcc \
    postgresql-dev \
    python3-dev \
    py3-psycopg2 \
    make \
    zlib-dev \
    jpeg-dev \
    libmagic \
    && \
    ln -s /usr/bin/python3 /usr/bin/python

# hack around https://github.com/pypa/pip/issues/6158#issuecomment-456619072
ENV PIP_DOWNLOAD_CACHE=/noop/
RUN \
    echo 'installing pip requirements' && \
    pip3 install --upgrade pip && \
    pip3 install setuptools wheel && \
    pip3 install -r /app/requirements.txt && \
    rm -rf $PIP_DOWNLOAD_CACHE

RUN mkdir /uploads /statics
VOLUME /uploads
VOLUME /statics

EXPOSE 8000
WORKDIR /app/
ENTRYPOINT ["./docker/entrypoint.sh"]
CMD ["./docker/server.sh"]
