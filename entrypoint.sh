#!/bin/sh
set -e

if ["$INSTALL_SENTRY" = "True"]; then
    pip install raven --upgrade
fi

exec "$@"
