import json

def login():
    print("login here\n")

    email=input("enter your email here")
    password=("enter your password here")

    with open ('staff.json') as json_file:
        data=json.loads (str(json_file.read()))

        if email==data["email"] and password == data["password"]:
            print("success")
        else:
            print("failed")