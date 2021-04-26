camgear
=====================

<a href="https://dev.sigpipe.me/dashie/camgear/src/branch/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg"/></a>
<img src="https://img.shields.io/badge/python-%3E%3D3.8-blue.svg"/> [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Requirements
- Python 3.8 (minimum !)
- Nginx
- PostgreSQL

# Install - manual

We assume in here you are installing under the `camgear` user with default home directory `/home/camgear`, like by doing:
```
useradd -m -s /bin/bash camgear
```

## API Backend

```shell
sudo su - camgear
git clone https://github.com/rhaamo/camgear/ camgear
cd camgear
python3.8 -m virtualenv -p python3.8 venv
source venv/bin/activate
pip install --requirement requirements.txt
# For production environment
cp deploy/env.prod.sample .env
$EDITOR .env
# For local development see the other section
python manage.py collectstatic
# don't forget to run migrations
python manage.py migrate
# create a superuser
python manage.py createsuperuser
```

You can uses `deploy/camgear-server.service` for your systemd service. 

## Nginx
See the file `deploy/camgear-nginx.conf` for a sample, don't forget you need all the `location /xxx` as the example to make it works.

## Development

For local development, you always needs to export `DJANGO_SETTINGS_MODULE=config.settings.local` to have the right config:
```
cp deploy/env.dev.sample .env
$EDITOR .env
export DJANGO_SETTINGS_MODULE=config.settings.local
python manage.py ...
```

### Docker image build
```
docker build -t camgear -f Dockerfile
```

## Updating
Look at release changes first if anything is needed.

```
sudo su - camgear
cd camgear
source venv/bin/activate
git pull
pip install -r requirements.txt
python manage.py migrate
```

Then restart your `camgear-server` service.

# Install - docker image
You can use the `Dockerfile` to run Camgear.

See the file ./deploy/env.prod.sample for the list of ENV variables you can use for the container.

You can copy that env file, edit it, and use `--env-file your-env-file.prod` for `docker run/exec` too.

The volume for uploads is `/uploads`.

To migrate the database:
```
docker exec -it camgear python manage.py migrate
```

To create your superuser:
```
docker exec -it camgear python manage.py createsuperuser
```

Example build & run:
```
docker build -t camgear -f Dockerfile .
docker run --net=host --name camgear -it --rm --env-file .env -v /local/path/to/uploads:/uploads camgear:latest
```

# Creating an user

Use the ``` python manage.py createsuperuser ``` command to create a super user.

# Licensing
 - MIT License
 