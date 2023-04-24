#!/bin/bash

# Check types
cd src && mypy --explicit-package-bases .; cd ..

# Run server
python src/main.py > /dev/null 2>&1 &
pid=$!

# Run celery
cd src && celery -A make_celery worker --loglevel INFO &

pwd

sleep 1

# Run tests
python src/bin/echo_client.py asdfff test /
python src/bin/echo_client.py asd test123 /
python src/bin/echo_client.py asd test123 /ticker/MSFT
python src/bin/echo_client.py asd test123 /ticker/VMW
python src/bin/echo_client.py asd test123 /tick

sleep 1

# Kill long-running services
kill $pid

cd src && celery -A make_celery control shutdown
cd ..