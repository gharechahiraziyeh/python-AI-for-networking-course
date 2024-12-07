from netmiko import ConnectHandler
from getpass import getpass

ip = input("Enter your device ip: ")
username = input("Enter your username: ")
password = getpass("Enter your password: ")

device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": username,
    "password": password,
    "port": "22"
}

command = ["interface loopback1", "ip addr 1.1.1.1 255.0.0.0"]

with ConnectHandler(**device) as ssh:
    output = ssh.send_config_set(command)
    
print(output)