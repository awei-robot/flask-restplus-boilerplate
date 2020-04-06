#!/bin/sh
cd /app
gunicorn manage:app -w 8 -b 0.0.0.0:5000 -k gevent --log-file ./gunicorn.log
