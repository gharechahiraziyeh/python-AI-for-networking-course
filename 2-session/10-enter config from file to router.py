from netmiko import ConnectHandler
import time


ip_lists = ["192.168.175.2", "192.168.175.3", "192.168.175.4"]

config_file = "config_file.txt"

for ip in ip_lists:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "root",
        "password": "1234",
        "port": "22"
    }
    with ConnectHandler(**device) as ssh:
        output = ssh.send_config_from_file(config_file)
        ssh.save_config()
        print(output)
        time.sleep(2)