import os
import subprocess
import signal

# print working directory:
print(os.getcwd())
print(subprocess.getoutput("ls -alh"))

# change current working directory:
os.chdir("/home/farhad")
print(subprocess.getoutput("ls -alh"))

# return list of files and directories:
print(os.listdir("/home/farhad/Desktop"))

# create a new directory:
os.mkdir("testpy")

# remove a directory:
os.rmdir("testpy")

# working with env:
print(os.environ)

# retries the value of a specific env:
print(os.environ.get("HOME"))

# set an env:
os.environ["TEST"] = "hello"
print(os.environ.get("TEST"))

# run a shell command:
os.system("ls")

# rename a file or directory:
os.rename("alarm1.mp3", "alarm2.mp3")

# remove a file or directory:
os.remove("output.txt")

# create a nested directory (exists_ok = True optional and for overwrite):
os.makedirs("level1/level2/level3", exist_ok=True)

# remove nested directory:
os.removedirs("level1/level2/level3")

# check if a path is file or directory:
print(os.path.isfile("/home/farhad/alarm2.mp3"))
print(os.path.isdir("/home/farhad/alarm2.mp3"))

# Getting system platform:
print(os.name)

# Getting system information:
print(os.uname())

# Get the current process id:
print(os.getpid())

# send kill signal to a process:
os.kill(25902, 9)
os.kill(25902, signal.SIGTERM)

# Get username:
print(os.getlogin())




