from netmiko import ConnectHandler

lab_switch = {
    'device_type': 'cisco_ios',
    'host':   '192.168.128.171',
    'username': 'cisco',
    'password': 'cisco',
    'port' : 22,          # optional, defaults to 22
}

net_connect = ConnectHandler(**lab_switch)

#output = net_connect.send_command('show ip int brief')
#print(output)

config_commands = [ 'no interface loopback2',
                    'description CONFIGURED_BY_PYTHON',
                    'ip add 2.2.2.2 255.255.255.255' ]
output = net_connect.send_config_set(config_commands)
print(output)

# This is a test
# This is a test 2
