from  createAccount import create_Account
from login import login


    
    
"""
register
login
exit
"""

print("this is fatima's alogorithim\n")
print("welcome\n create your account")
def options():
    register =input("enter 1 to register\n or 2 to create account")

    if register =="1":
        login()
    elif register =="2":
        create_Account()


def source():
    options()
source()


    


    
    