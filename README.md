# CamGear

<a href="https://dev.sigpipe.me/dashie/camgear/src/branch/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg"/></a>
<img src="https://img.shields.io/badge/python-%3E%3D3.8-blue.svg"/> [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Requirements
- Python 3
- Nginx
- PostgreSQL

# Install - manual

We assume in here you are installing under the `camgear` user with default home directory `/home/camgear`, like by doing:
```
useradd -m -s /bin/bash camgear
```

## The App

```shell
sudo su - camgear
git clone https://github.com/rhaamo/camgear/ camgear
python -m virtualenv venv
source venv/bin/activate
cd camgear
pip install --requirement requirements.txt
# For production environment
cp deploy/env.prod.sample .env
$EDITOR .env
# don't forget to run migrations
python manage.py migrate
# import django admin theme
python manage.py loaddata admin_interface_theme_foundation.json
# For local development you don't need that
python manage.py collectstatic
# create a superuser
python manage.py createsuperuser
```

You can uses `deploy/camgear-server.service` for your systemd service. 

## Nginx
See the file `deploy/camgear-nginx.conf` for a sample, don't forget you need all the `location /xxx` as the example to make it works.

## Development

For local development you need to set the env variable `DEBUG` to `TRUE`:
```
export DEBUG=True
python manage.py ...
python manage.py runserver_plus 0.0.0.0:8080
...
```

### Docker image build
```
docker build -t camgear -f Dockerfile
```

## Updating
Look at release changes first if anything is needed.

```
sudo su - camgear
source venv/bin/activate
cd camgear
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
```

Then restart your `camgear-server` service.

# Install - docker image
You can use the `Dockerfile` to run Camgear.

See the file ./deploy/env.prod.sample for the list of ENV variables you can use for the container.

You can copy that env file, edit it, and use `--env-file your-env-file.prod` for `docker run/exec` too.

The volume for uploaded files is `/uploads`.

The volume for static files is `/statics`.

To migrate the database:
```
docker exec -it camgear /venv/bin/python manage.py migrate
```

To create your superuser:
```
docker exec -it camgear /venv/bin/python manage.py createsuperuser
```

Example build & run:
```
docker build -t camgear -f Dockerfile .
docker run --net=host --name camgear -it --rm --env-file .env -v /local/path/to/uploads:/uploads -v /local/path/to/statics:/statics camgear:latest
```

# Creating an user

Use the `python manage.py createsuperuser` command to create a super user.

# Licensing
 - MIT License