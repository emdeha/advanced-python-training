#!/bin/bash

cd src && mypy --explicit-package-bases . && cd ..

python src/main.py > /dev/null 2>&1 &
pid=$!

sleep 0.1

python src/bin/echo_client.py asd test /
python src/bin/echo_client.py asd test123 /
python src/bin/echo_client.py asd test123 /ticker/MSFT
python src/bin/echo_client.py asd test123 /tick

kill $pid