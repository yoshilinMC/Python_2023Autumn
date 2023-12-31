import pyrebase
from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  "apiKey": "AIzaSyC64F1MZ-6OlPjltmUD4p4zgVbSJ5PBBGY",
  "authDomain": "fir-tesk-e1ace.firebaseapp.com",
  "projectId": "fir-tesk-e1ace",
  "storageBucket": "fir-tesk-e1ace.appspot.com",
  "messagingSenderId": "2415330990",
  "appId": "1:2415330990:web:7179784cb37b2b30148f3f",
  "measurementId": "G-ZG5V9XWMKY",
  "databaseURL" : ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

root = Tk()

# Labels
loginlabel = Label(root,text="Login page")
acountlabel = Label(root,text="Account")
passwordlabel = Label(root,text="Password")
resultlabel = Label(root,text="")

# Entry
accountEntry = Entry(root)
passwordEntry = Entry(root, show="*")

# Button
signupButton = Button(root, text="Sign up", width=10,command=lambda: signup(root,accountEntry,passwordEntry))
LoginButton = Button(root, text="login", width=10,command=lambda: login(root,accountEntry,passwordEntry))

# pack
loginlabel.pack(pady=5)
acountlabel.pack(pady=5)
accountEntry.pack(pady=5)
passwordlabel.pack(pady=5)
passwordEntry.pack(pady=5)
signupButton.pack(pady=5)
LoginButton.pack(pady=5)
resultlabel.pack(pady=5)

def signup(view,accountentry,passwordentry):
    print(accountentry.get(),passwordentry.get())
    print("Sign up")
    account = accountEntry.get()
    password = passwordEntry.get()
    try:
      user = auth.create_user_with_email_and_password(account,password)
      print("successfully signup")
      resultlabel.config(text="succesfully sign up")
    except Exception as e:
      print(f"fail to sign up : {e}")
      resultlabel["text"] = "Create user failed"

def login(view,accountentry,passwordentry):
    print(accountentry.get(),passwordentry.get())
    print("login in ...")
    account = accountEntry.get()
    password = passwordEntry.get()
    try:
      user = auth.sign_in_with_email_and_password(account,password)
      print("successfully login")
      resultlabel.config(text="succesfully login")
    except Exception as e:
      print(f"fail to login : {e}")
      resultlabel["text"] = "Login failed"

root.mainloop()