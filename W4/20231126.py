# python
import pyrebase

"""
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

def signup():
    email = input("please enter your email: ")
    password = input("please enter your password: ")
    # user = auth.create_user_with_email_and_password(email,password)
    # print("successfully signup")
    try:
      user = auth.create_user_with_email_and_password(email,password)
      print("successfully signup")
    except:
      print("email acount has already exist")
def login():
    print("Login in...")
    email = input("enter your email: ")
    password = input("enter your password: ")
    try:
      login = auth.sign_in_with_email_and_password(email,password)
      print(login["localId"])
      print("Successfully logged in!")
    except:
      print("Invalid email or password!")

# signup()
login()
"""
"""
class car:
    def __init__(self,color):
        self.color = color
        self.next = None
head = car("red")
head.next = None

def traverse(head):
    ptr = head
    while ptr != None:
        print("The color of the car is {}".format(ptr.color))
        ptr = ptr.next
    print("Finish traverse")

traverse(head)
"""

class student:
    def __init__(self,name,score):
      self.name = name
      self.score = score
      self.next = None
name = student("bob",88)
name.next = None

def traverse(name):
    ptr = name
    while ptr != None:
        print("The student name is {} and the math score is {}".format(ptr.name,ptr.score))
        ptr = ptr.next
    print("Finish traverse")

traverse(name)