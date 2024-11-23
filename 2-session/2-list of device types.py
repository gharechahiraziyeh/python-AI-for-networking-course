from netmiko import ConnectHandler

device = {
    "device_type": "invalid",
    "host": "192.168.175.2",
    "username": "root",
    "password": "1234",
    "port": "22"
}

with ConnectHandler(**device) as ssh:
    print(ssh.find_prompt())