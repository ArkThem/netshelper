from random import randint


def get_lines(filepath: str):
    with open(filepath, "r") as f:
        return f.readlines()
    
def add_line(filepath: str, line: str):
    current = get_lines(filepath)
    current.append(line)
    current = (x.strip().replace('\r', '').replace('\n', '') for x in current)
    with open(filepath, 'w') as f:
        f.write("\n".join(current))
        
def get_next_ip(ip: str):
    subnets = list([int(x) for x in ip.split('.')])
    if subnets[-1] == 254:
        subnets[-1] = 1
        if subnets[-2] == 254:
            subnets[-2] = 1
            if subnets[-3] == 254:
                raise Exception("There is no more IP in 127.0.0.0/8")
            subnets[-3] += 1
        subnets[-2] += 1
    subnets[-1] += 1
    return '.'.join((str(x) for x in subnets))

def get_random_ip():
    return f"127.{randint(1, 254)}.{randint(1, 254)}.{randint(1,254)}"
