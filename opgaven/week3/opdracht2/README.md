## Running docker

1. Download and install [Docker Toolbox](https://www.docker.com/toolbox)  
2. Run `Docker Quickstart Terminal` to setup a default docker machine (this may take a while)  
3. Open powershell  
4. execute `docker-machine ls` to see the status and ip of the default machine  
5. execute `docker-machine env default --shell=powershell | Invoke-Expression`  
6. execute `./build.bat` to build the docker image named `hanze-nrg`  
7. execute `./run.bat` to run the docker  
8. open `http://<machine_ip>:5000` to view the website. (default ip is `192.168.99.100`, use `docker-machine ls` to check)

### troubleshooting

if you get the following error:
```
No connection could be made because the target machine actively refused it..
* Are you trying to connect to a TLS-enabled daemon without TLS?
* Is your docker daemon up and running?
```

Try and run this command again:
```
docker-machine env default --shell=powershell | Invoke-Expression
```