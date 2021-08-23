from os import remove
import random
import json

def create_Products():
    id=random.randint(0,9)
    title=input("enter product name\n")
    quantity=input(int("enter the quantity\n"))
    price=input(float("enter the price\n"))

    data={
        'id':id,
        'title':title,
        'quantity':quantity,
        'price':price

    }
    with open ('products.json','w+') as filename:
        json.dump(data,filename,indent=1)
        
def readproduct():
    with open('products.json') as filename:
        data=json.loads(str(filename.read()))
        print("name of product",data["title"])
        print ("quantity",data['quantity'] )
        print("price",data['price'])

def updateproduct():
    with open ('products.json')as filename:
        data=json.loads(str(filename.read()))
        print('existing data',data) 

        data={
            'id':random.randint(0,9),
            'title':"cream",
            'quantity':2,
            'price':5000
        }   
        with open ('product.json','w+') as file:
            json.dump(data,file,indent=1)
            print("data has been updated\n")

def deleteproduct():
    remove('product.json')
