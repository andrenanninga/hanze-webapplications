@echo off

:: set `drive` as current drive without path
set drive=%~d0
:: remove trailing ":"
set drive=%drive:~0,1%
:: make lowercase
set drive=%drive:C=c%
set drive=%drive:D=d%
set drive=%drive:E=e%

:: set `directory` as current path without drive
set directory=%~p0
:: replace backslashes with forward slashes
set directory=%directory:\=/%

:: set `srcdir` as "/"+`drive`+`directory`+"src"
set srcdir=/%drive%%directory%src

:: save full command to run docker
set command=docker run^ -it -p 5000:5000 -v %srcdir%:/flask/src hanze-nrg

:: echo command for manual use
echo %command%

:: run command
%command%