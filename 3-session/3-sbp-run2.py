import subprocess as sbp

output = sbp.run(["ping", "4.2.2.4"], capture_output=True)
#print(f" the output type is {type(output)}")
print(output)
with open("output.txt", "w") as file:
    result = sbp.run(["ping", "4.2.2.4"], stdout=file)