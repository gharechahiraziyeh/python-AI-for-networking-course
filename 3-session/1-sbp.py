import subprocess as sbp

ip = "4.2.2.4"
output = sbp.getoutput(f"ping {ip} ")
print(f" the output type is {type(output)}")
print(output)
