#!/bin/bash -eux
/venv/bin/python /app/manage.py migrate
/venv/bin/python manage.py loaddata admin_interface_theme_foundation.json
/venv/bin/python /app/manage.py collectstatic --noinput
cd /app/
/venv/bin/gunicorn --log-file=- --worker-tmp-dir /dev/shm camgear.asgi:application -w ${CAMGEAR_WEB_WORKERS-2} --threads ${CAMGEAR_WEB_THREADS-4} -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 ${GUNICORN_ARGS-}
