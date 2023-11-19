import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/Thomas Muldoon/Desktop/tm-lc-cs-firebase-adminsdk-w6jfd-859924f9b8.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://tm-lc-cs-default-rtdb.europe-west1.firebasedatabase.app/'})
 
ref = db.reference().child('classes')

results = ref.get()
#print(results)
#print(type(results))
for k,v in results.items():
    print("Key is:", k, "\t value is: ",v)
    for k2, v2 in v.items():
        print("Key is:", k2, "\t value is: ",v2)