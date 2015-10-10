#!/bin/bash

echo "Starting mysql"
/etc/init.d/mysql start

echo "Creating nrg database"
mysql -uroot -e "create database nrg;"

echo "Creating nrg tables"
mysql -uroot nrg < /flask/sql/nrg.sql

echo "Creating nrg stored procedures"
mysql -uroot nrg < /flask/sql/nrg_storedprocedures.sql

echo "Inserting sample data"
mysql -uroot nrg < /flask/sql/nrg_init.sql

echo "Setup 'root' as password for user 'root'"
mysql -uroot -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root'); GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root';"
