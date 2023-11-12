# import packages
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:/Users/yoshi/Desktop/Python/Python_2023Autumn/key.json")
firebase_admin.initialize_app(cred)