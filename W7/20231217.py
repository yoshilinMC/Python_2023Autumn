import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# import secret key
# key.json
cred = credentials.Certificate("key.json")
# initiate firebase
firebase_admin.initialize_app(cred)
# initiate firestore
db = firestore.client()

# doc = { "name":"Yoshi","Email":"yoshilin77@gmail.com"}
# doc_ref = db.collection("Autumn_students").document("student01")
# doc_ref.set(doc)

# collection_ref = db.collection("Autumn_students")
# collection_ref.add(doc)

# doc = { "name":"Jaclyn","Email":"jaclyn@gmail.com"}
# doc_ref = db.collection("Autumn_students").document("student02")
# doc_ref.set(doc)

# path = "Autumn_students/student02"
# doc_ref = db.document(path)

# try :
#     doc = doc_ref.get()
#     doc_dict = doc.to_dict()
#     print("The content of the document is {}".format(doc_dict))
# except :
#     print("The reference of document is not exist , please check the path is correct or not.")

# path = "Autumn_students"
# collection_ref = db.collection(path)
# docs = collection_ref.where("name","==","Jaclyn").get()
# for doc in docs :
#     print("The content of the document is : {}".format(doc.to_dict()))

# path = "Autumn_students/student01"
# doc_ref = db.document(path)
# doc = {"birthday":"0412"}
# doc_ref.update(doc)

# path = "Autumn_students/student01"
# doc_ref = db.document(path)
# contacts = {"Email":"yoshilin77@gmail.com","PhoneNumber":"0910748511"}
# doc = {"contacts":contacts}
# doc = {"contacts.Email":"niceday@gmail.com"}
# doc_ref.update(doc)

# path = "Autumn_students/student02"
# doc_ref = db.document(path)
# doc_ref.delete()

student_ref = db.collection("Autumn_students")
docs = student_ref.get()
for doc in docs :
    doc.reference.delete()