from subprocess import run
from utils import get_random_ip
from hosts import add_hosts_record, delete_hosts_record


def add_netsh_rule(
    ip: str, 
    port_ip: int, 
    domain: str, 
    port_domain: int
    ):
    hosts_ip = get_random_ip()
    add_hosts_record(hosts_ip, domain)
    run(f"netsh interface portproxy add v4tov4 listenport={port_domain} listenaddress={hosts_ip} connectport={port_ip} connectaddress={ip}")
    
def remove_netsh_rule(ip_hosts: str):
    run(f'netsh interface portproxy delete v4tov4 listenport=80 listenaddress={ip_hosts}')
    delete_hosts_record(ip_hosts)


