import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.open()

cred = credentials.Certificate("C:/Users/Thomas Muldoon/Desktop/tm-lc-cs-firebase-adminsdk-w6jfd-859924f9b8.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://tm-lc-cs-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference()
ref.update({'temperature_log':''})
ref = db.referance().child('temperature_log')

source = input("Please input the source of this data: ")
i = 0
while True:
    #print(type(ser.readline()))
    mb_temperature = str(ser.readline().decode('utf-8'))
    #print(len(mb_temperature))
    
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    print("Len of temp is: ", len(mb_temperature))
    print(mb_temperature)
    
    if mb_temperature.isdigit():
        ref.update({'Reading' + str(i):{'Temperature':mb_temperature, 'Location':source}})
        i = i+1
    else:
        print("Check data source")