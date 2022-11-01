import re

usernm=input("Enter username:")
unm_pattern="[A-Z]+[a-z]+[0-9]" #pattern

x=re.findall(unm_pattern,usernm)

if x:
    print("Username is valid!")
else:
    print("Error!Invalid Username.")