#!/bin/bash

echo "Starting mysql"
/etc/init.d/mysql start

echo "Creating nrg database"
mysql -uroot -e "create database nrg;"

echo "Creating nrg tables"
mysql -uroot nrg < /flask/sql/nrg.sql

echo "Creating nrg stored procedures"
mysql -uroot nrg < /flask/sql/nrg_storedprocedures.sql

echo "Setup 'root' as password for user 'root'"
mysql -uroot -e "FLUSH PRIVILEGES; SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root')"