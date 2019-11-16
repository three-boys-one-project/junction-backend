import json
import requests
import time
import pyrebase

config = {
  "apiKey": "AIzaSyBra07LSvzKcKiicYI32rINLsva8Ozf5D4",
  "authDomain": "boys-for-junction.firebaseapp.com",
  "databaseURL": "https://boys-for-junction.firebaseio.com",
  "storageBucket": "boys-for-junction.appspot.com",
  "serviceAccount": "../boys-for-junction-firebase-adminsdk-mq573-34deda5cac.json"
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

url = 'http://13.48.149.61:8000/notify.json'

get_mac = lambda a: a['notifications'][0]['deviceId']
get_coor = lambda a: a['notifications'][0]['locationCoordinate']
get_map = lambda a: a['notifications'][0]['locationMapHierarchy']


# db.child('mp').child('durmac').set({'x':str(1.06), 'y':str(1.03)})

with open('json_fin.json', 'r') as fd:
    a = json.load(fd)

for i in a:
    for j in i.keys():
        for k in i[j].keys():
            dicc = {'map':j}
            dicc.update(i[j][k])
            db.child(k).set(dicc)

    # db.child(a[i][])
