import pyrebase
import os

config = {
  "apiKey": "AIzaSyC64F1MZ-6OlPjltmUD4p4zgVbSJ5PBBGY",
  "authDomain": "fir-tesk-e1ace.firebaseapp.com",
  "projectId": "fir-tesk-e1ace",
  "storageBucket": "fir-tesk-e1ace.appspot.com",
  "messagingSenderId": "2415330990",
  "appId": "1:2415330990:web:7179784cb37b2b30148f3f",
  "measurementId": "G-ZG5V9XWMKY",
  "databaseURL" : "",
  "serviceAccount" : "C:/Users/yoshi/Desktop/Python/Python_2023Autumn/key.json"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

dir_name = "nature"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

all_files = storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name):
        file.download_to_filename(file.name)