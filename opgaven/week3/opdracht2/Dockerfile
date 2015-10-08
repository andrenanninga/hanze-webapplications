FROM ubuntu:14.04

# setup working directory /flask
RUN mkdir /flask
VOLUME ["/flask"]

# install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y upgrade

# install mysql
RUN apt-get install -y mysql-server libmysqlclient-dev

# install python2.7
RUN apt-get install --no-install-recommends -y -q build-essential python2.7 python2.7-dev python-pip git
RUN pip install -U pip
RUN pip install virtualenv

# install pip packages
ADD requirements.txt /flask/requirements.txt
RUN pip install --no-cache-dir -r /flask/requirements.txt

# add src/run.py to /flask
ADD src/run.py /flask/run.py

# enable remote access for mysql (default is localhost only, we change this
# otherwise our database would not be reachable from outside the container)
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

RUN service start mysqld

# expose flask devserver port
EXPOSE 5000

# expose mysql port
EXPOSE 3306

# run flask app
# CMD python /flask/run.py