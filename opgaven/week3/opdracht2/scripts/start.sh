#!/bin/bash

echo "Starting mysql"
/etc/init.d/mysql start

echo "Starting flask"
python /flask/src/run.py