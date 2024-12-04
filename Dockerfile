FROM alpine:edge

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
    py3-pip \
    py3-virtualenv \
    make \
    zlib-dev \
    jpeg-dev \
    libmagic

# hack around https://github.com/pypa/pip/issues/6158#issuecomment-456619072
ENV PIP_DOWNLOAD_CACHE=/noop/
RUN \
    echo 'installing pip requirements' && \
    python -m virtualenv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install setuptools wheel && \
    /venv/bin/pip install -r /app/requirements.txt && \
    rm -rf $PIP_DOWNLOAD_CACHE

RUN mkdir /uploads /statics
VOLUME /uploads
VOLUME /statics

EXPOSE 8000
WORKDIR /app/
ENTRYPOINT ["./docker/entrypoint.sh"]
CMD ["./docker/server.sh"]
