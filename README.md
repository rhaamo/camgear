camgear
=====================

<a href="https://dronegh.sigpipe.me/rhaamo/camgear"><img src="https://dronegh.sigpipe.me/api/badges/rhaamo/camgear/status.svg" alt="Build Status"/></a>
<a href="https://dev.sigpipe.me/dashie/camgear/src/branch/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg"/></a>
<img src="https://img.shields.io/badge/python-%3E%3D3.6-blue.svg"/> [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Versions requirement
 - Python >= 3.6 (all under 3.6 are not supported) (say bye-bye to debian stable, sorry)
 - try https://github.com/chriskuehl/python3.6-debian-stretch if you use debian stable

# Installation
    Install a BDD (mysql is supported, SQLite maybe, PostgreSQL should be)
    Makes sure that encoding is/will be in UNICODE/UTF-8
    git clone https://github.com/rhaamo/camgear
    cd camgear
    pip3 install --requirement requirements.txt
    python3 setup.py install
    cp config.py.sample config.py
    $EDITOR config.py
    export FLASK_ENV=<development or production>
    $ create your postgresql database, like 'camgear'
    flask db upgrade
    flask seed
    flask run

# Creating an user

If you have enabled registration in config, the first user registered will be ADMIN !

Or if you have disabled registration, use the ``` flask createuser ``` command to create an user.

# Production running

    sudo easy_install3 virtualenv
    sudo su - camgear
    cd camgear
    
    >> install -> git part
    
    virtualenv -p /usr/bin/python3 venv
    or if python 3.6 from github repo:
    virtualenv -ppython3.6 venv
    
    source venv/bin/activate
    >> get back to install part
    
    pip install waitress
    
# Docker

TODO

# Licensing
 - MIT License
 