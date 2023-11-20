import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
def something_Changed(response):
    print(response.event_type)
    print(response.data)
    
cred = credentials.Certificate("C:/Users/Thomas Muldoon/Desktop/tm-lc-cs-firebase-adminsdk-w6jfd-859924f9b8.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://tm-lc-cs-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference().child('temperature_log')
my_ref = ref.listen(something_Changed)