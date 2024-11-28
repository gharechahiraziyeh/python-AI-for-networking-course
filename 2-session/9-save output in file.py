from netmiko import ConnectHandler
import time
import datetime


ip_lists = ["192.168.175.2", "192.168.175.3", "192.168.175.4"]

command = ["interface loopback 1", "ip add 1.1.1.1 255.0.0.0"]

for ip in ip_lists:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "root",
        "password": "1234",
        "port": "22"
    }
    with ConnectHandler(**device) as ssh:
        backup_name = ssh.find_prompt().strip("#") + "_"
        date = str(datetime.date.today())
        backup_name =backup_name + date
        output = ssh.send_config_set(command)
        ssh.save_config()
        print(output)
        with open(backup_name, "w") as file:
            file.write(output)
        time.sleep(2)