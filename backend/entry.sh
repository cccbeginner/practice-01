#!/bin/sh
echo 'enter!!!!!!!!!!!!!!!!!!!!!!!'
export DB_HOST=$(awk '/db/ {print $1}' /etc/hosts)
exho $DB_HOST
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
