#!/bin/sh
set -e

export STATIC_ROOT=/statics
export MEDIA_ROOT=/uploads

exec "$@"