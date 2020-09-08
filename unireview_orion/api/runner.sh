#!/usr/bin/env sh

uwsgi --http "0.0.0.0:${PORT}" --wsgi-file unireview_orion/wsgi.py --need-app --master --processes 4 --threads 2
