from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys
import argparse

parser = argparse.ArgumentParser(description='Get group ID  from zabbix by name' )
parser.add_argument('-n', '--hostname', type=str)
parser.add_argument('-l', '--login', type=str)
parser.add_argument('-u', '--url_server', type=str)
parser.add_argument('-p', '--password', type=str)

def check_arg(checked_arg):
    if checked_arg is not None:
        return checked_arg
    else:
        print("try -h for usage")
        raise SystemExit    

args = parser.parse_args()

host_name = check_arg(args.hostname)
zabbix_url = check_arg(args.url_server)
zabbix_user = check_arg(args.login)
zabbix_password = check_arg(args.password)


zapi = ZabbixAPI(url=zabbix_url, user=zabbix_user, password=zabbix_password)

hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])

if hosts:
    host_id = hosts[0]["hostid"]
    print("{0}".format(host_id))
