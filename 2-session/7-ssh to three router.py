from netmiko import ConnectHandler
import time

device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.175.2",
    "username": "root",
    "password": "1234",
    "port": "22"
}

device2 = {
    "device_type": "cisco_ios",
    "host": "192.168.175.3",
    "username": "root",
    "password": "1234",
    "port": "22"
}

device3 = {
    "device_type": "cisco_ios",
    "host": "192.168.175.4",
    "username": "root",
    "password": "1234",
    "port": "22"
}




command = ["interface loopback 1", "ip add 1.1.1.1 255.0.0.0"]

device_list = [device1, device2, device3]

for device in device_list:
    with ConnectHandler(**device) as ssh:
        output = ssh.send_config_set(command)
        ssh.save_config()
        time.sleep(2)