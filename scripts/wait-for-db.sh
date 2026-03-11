#!/bin/sh

host="$POSTGRES_HOST"
port="$POSTGRES_PORT"

echo "Waiting for postgres..."

while ! nc -z $host $port; do
  sleep 1
done

echo "PostgreSQL started"