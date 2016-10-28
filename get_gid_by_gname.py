from zabbix.api import ZabbixAPI
import argparse

parser = argparse.ArgumentParser(description='Get group ID  from zabbix by name' )
parser.add_argument('-g', '--groupname', type=str, help="use \"\" if contain spaces")
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

gname = check_arg(args.groupname)
zabbix_url = check_arg(args.url_server)
zabbix_user = check_arg(args.login)
zabbix_password = check_arg(args.password)


# Create ZabbixAPI class instance
zapi = ZabbixAPI(url=zabbix_url, user=zabbix_user, password=zabbix_password)

# Get host item value
gid = zapi.hostgroup.get(filter={"name": gname})
print(gid[0]['groupid'])
