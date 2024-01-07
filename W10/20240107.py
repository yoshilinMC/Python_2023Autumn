import os
import firebase_admin
from firebase_admin import credentials, storage
cred = credentials.Certificate("../key.json")
firebase_admin.initialize_app(cred,{"storageBucket":"fir-tesk-e1ace.appspot.com"})

dir_path = "./Firebase_project/image"
filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg")]
print(filelist)

bucket = storage.bucket()
for file in filelist:
    file_path = dir_path+"/"+file
    blob_path = "project_images/"+file
    print("Now is uploading file {}".format(file_path))
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)