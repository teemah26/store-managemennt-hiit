import json 
import random

def create_Account():
    id=random.randint(1,10)
    email=input("enter your email")
    password=input("enter your password")

    data={
        'id':id,
        'email':email,
        'password':password

    }
    print("account created successfully\n")

    with open ('staff.json','a+') as jsonfile:
        json.dump(data,jsonfile,indent=1)