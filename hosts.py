from utils import add_line, get_lines


HOST_FILE = r'C:\Windows\System32\drivers\etc\hosts'

def add_hosts_record(ip: str, domain: str):
    line = f"{ip} {domain} #netsh_rule"
    add_line(HOST_FILE, line)
    
def get_hosts_netshhelper_records():
    return list([x for x in get_lines(HOST_FILE) if "#netsh_rule" in x])
    
def delete_hosts_record(ip: str):
    lines = get_lines(HOST_FILE)
    lines = [x.strip() for x in lines if f"{ip}" not in x]
    with open(HOST_FILE, 'w') as f:
        f.write("\n".join(lines))
        
