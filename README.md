# netshelper
Create hosts records with ports on Windows, using netsh prox, just run python main.py with administator rights.

Here the source: https://stackoverflow.com/questions/8652948/using-port-number-in-windows-host-file

The rule must looks like ip:port domain:domain_port:
- domain_port usually 80 or 443, depends of the http or http connection you use
