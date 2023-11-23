import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial


cred = credentials.Certificate("C:/Users/18TMuldoon.ACC/OneDrive - Longford and Westmeath Education and Training Board/Com-Science/tm-lc-cs-firebase-adminsdk-w6jfd-859924f9b8.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://tm-lc-cs-default-rtdb.europe-west1.firebasedatabase.app/'})

# this connects to microbit
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

while True:
    toggle = "1\n"
    ser.write(toggle.encode('utf-8'))
    time.sleep(5)
    toggle = "0\n"
    ser.write(toggle.encode('utf-8'))
    time.sleep(5)