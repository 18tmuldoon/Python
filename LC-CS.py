import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/Thomas Muldoon/Desktop/tm-lc-cs-firebase-adminsdk-w6jfd-859924f9b8.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://tm-lc-cs-default-rtdb.europe-west1.firebasedatabase.app/'})

#ref = db.reference('/')

#ref.update({'class_enrolments':''})
#ref.update({'classes':''})

#ref = db.reference().child('class_enrolments')
#ref.update({'Biology123':''})
#ref.update({'Math123':''})

#ref = db.reference().child('class_enrolments').child('Biology123')
#ref.update({'JohnDoe123':True})
#ref.update({'JaneDoe123':True})
#ref = db.reference().child('class_enrolments').child('Math123')
#ref.update({'JaneDoe123':True})

#ref = db.reference().child('classes').child('Biology123')
#ref.update({'Description':'Biology123 class', 'id':'Biology123', 'title':'Biology 123'})
#ref = db.reference().child('classes').child('Math123')
#ref.update({'Description':'Math123 class', 'id':'Math123', 'title':'Math 123'})

#ref = db.reference().child('classes').child('Biology123')
#ref.delete()