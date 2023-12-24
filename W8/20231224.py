import firebase_admin
from firebase_admin import credentials, storage
cred = credentials.Certificate("../key.json")
firebase_admin.initialize_app(cred,{"storageBucket":"fir-tesk-e1ace.appspot.com"})

file_path = "Firebase_project/image/bed1.jpg"
bucket = storage.bucket() # storage bucket
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)