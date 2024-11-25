import subprocess as sbp

ip = "4.2.2.4"
output = sbp.run(["ping", "4.2.2.4"])
print(f" the output type is {type(output)}")
print(output)