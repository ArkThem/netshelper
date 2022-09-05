from netsh import add_netsh_rule, remove_netsh_rule
from hosts import get_hosts_netshhelper_records


def add_choice():
    rule = input("Write rule like 127.0.0.1:9999 mydomain: \n")
    ip_port, domain = rule.split(' ')
    ip, port = ip_port.split(':')
    add_netsh_rule(ip=ip, port=int(port), domain=domain)
    print(rule + 'added succesfully')
    
def delete_choice():
    print('Which record to delete? Write number:')
    records = [x.replace('#netsh_rule', '').strip() for x in get_hosts_netshhelper_records()]
    for i, record in enumerate(records, start=1):
        print(f"{i}. {record.replace('#netsh_rule', '')}")
    del_choice = int(input())
    ip_del, _ = records[del_choice-1].split(" ")
    remove_netsh_rule(ip_del)
    print(f"{records[del_choice-1]} has been deleted succesfully")
    
        
choise_start = input("Delete or add rule?\n1. Add netsh rule\n2. Delete netsh rule\n3. Exit\n:")
match choise_start:
    case '1':
        add_choice()
    case '2':
        delete_choice()
    case _:
        exit()
# rule = input("Write rule like 127.0.0.1:9999 mydomain: \n")