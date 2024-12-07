import time
from getpass import getpass
from netmiko import ConnectHandler
import matplotlib.pyplot as plt


device1 = {
    "device_type" : "cisco_ios",
    "host": "192.168.175.2",
    "username": "root",
    "password": "1234",
    "port": "22"
}

device2 = {
    "device_type" : "cisco_ios",
    "host": "192.168.175.3",
    "username": "root",
    "password": "1234",
    "port": "22"
}


device_list = [device1, device2]
output_list = []
input_list = []
x1 = []
x = 10


while x > 0:
    for device in device_list:
        with ConnectHandler(**device) as ssh:
            output = ssh.send_command("sho int gi0/0")
            print(output)
            time.sleep(2)
        
    input1 = output.split("(size/max)\n  ")
    input2 = input1[1]
    input2 = input2.split("minute")
    input2 = input2[0]
    print("input:", int(input2))
    output = str(input2).split("packets/sec")
    output = output[0]
    print("output:", int(output))
    x -= 1
    input_list.append(int(input2))
    output_list.append(int(output))
    print(input_list)
    print(output_list)
    x1.append(x)
    print(x1)
    time.sleep(1)
    
    
plt.plot(x1, input_list, color="blue", marker="o", linestyle="--", label="input rate")
plt.plot(x1, output_list, color="red", marker="o", linestyle="-.", label="output rate")
plt.xlabel("x")
plt.ylabel("input-output rate")
plt.title("input time rate and output time rate")
plt.legend()
plt.savefig("input-output.jpg", dpi=300)
plt.show()
    
        
    
    