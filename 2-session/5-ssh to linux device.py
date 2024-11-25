from netmiko import ConnectHandler

ip = "192.168.157.129"
device = {
    "device_type": "linux",
    "host": ip,
    "username": "razi",
    "password": "4027",
    "port": "22"
}

with ConnectHandler(**device) as ssh:
    output = ssh.send_command("ls > ls.txt")
    print(output)