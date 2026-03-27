import os

def check_login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

user = input("Enter username: ")
pwd = input("Enter password: ")

if check_login(user, pwd):
    cmd = input("Enter command to execute: ")
    os.system(cmd)
else:
    print("Invalid credentials")
