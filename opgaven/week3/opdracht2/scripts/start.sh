#!/bin/bash

echo "Starting mysql"
/etc/init.d/mysql start

echo "Starting flask"
python -B /flask/src/run.py