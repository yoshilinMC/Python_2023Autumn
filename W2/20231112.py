# import packages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("C:/Users/yoshi/Desktop/Python/Python_2023Autumn/key.json")
firebase_admin.initialize_app(cred)

# def funtion(n, a=1,b=2):
#     print(n+a+b)

# def funtion(n, *args):
#     print(n)
#     print(args)

email = "yoshilin77@gmail.com"
password = "123456"

user = auth.create_user(email=email,password=password)
print("User create successfully! {}".format(user.uid))