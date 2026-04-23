import re

psswd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!$#%^&*()])[a-zA-Z\d!@#$%^&*()]{8,20}$"

def validate(passwd):
    return bool(re.findall(psswd,passwd))

p = input("Enter a password sequence: ")

if validate(p):
    print("The entered password is strong")
else: print("The entered password is weak")
