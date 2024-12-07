from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.175.2",
    "username": "root",
    "password": "1234",
    "port": "22"
}

command = "interface loopback 1"
with ConnectHandler(**device) as ssh:
    output = ssh.send_config_set(command)
    print(output)