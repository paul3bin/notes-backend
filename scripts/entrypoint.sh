#!/bin/sh

set -e

uwsgi --socket :8000 --master --enable-threads --module notes_api.wsgi