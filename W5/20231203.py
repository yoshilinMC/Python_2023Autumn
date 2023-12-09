"""
import pyrebase
from tkinter import *

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

# pack
loginlabel.pack(pady=5)
acountlabel.pack(pady=5)
accountEntry.pack(pady=5)
passwordlabel.pack(pady=5)
passwordEntry.pack(pady=5)
signupButton.pack(pady=5)
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

# def login():
#     print("Login in...")
#     email = input("enter your email: ")
#     password = input("enter your password: ")
#     try:
#       login = auth.sign_in_with_email_and_password(email,password)
#       print(login["localId"])
#       print("Successfully logged in!")
#     except:
#       print("Invalid email or password!")

root.mainloop()
"""

class car:
    def __init__(self,color):
        self.color = color
        self.next = color
        self.next = color
        self.next = None
head = car("blue")
head.next = car("red")
head.next.next = car("black")

def traverse(head):
    ptr = head
    while ptr != None:
        print("The color of the car is {}".format(ptr.color))
        ptr = ptr.next
    print("Finish traverse")

traverse(head)