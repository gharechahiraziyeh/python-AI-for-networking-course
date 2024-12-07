import hashlib
import time
real_hash = "f78096cafcc8ba9564e5478b3b4641df34bb541eb59366d5614491a495ab642f"
file_path = "/home/razi/Desktop/python-AI-for-networking-course/1-session/hash-checked.txt"
file = open(file_path, "rb").read()
calculated_hash = hashlib.sha256(file).hexdigest()

while True:
    if calculated_hash == real_hash:
        print("every thing is OK!")
    else:
        print(f"Danger!!!! {file_path} is modified")


    time.sleep(2)