from subprocess import run


run('netsh interface portproxy delete v4tov4 listenport=80 listenaddress=127.24.200.56')