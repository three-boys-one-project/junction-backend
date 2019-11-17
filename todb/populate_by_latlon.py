import json
import requests
import time
import pyrebase
import re

config = {
  "apiKey": "AIzaSyBra07LSvzKcKiicYI32rINLsva8Ozf5D4",
  "authDomain": "boys-for-junction.firebaseapp.com",
  "databaseURL": "https://boys-for-junction.firebaseio.com",
  "storageBucket": "boys-for-junction.appspot.com",
  "serviceAccount": "../boys-for-junction-firebase-adminsdk-mq573-34deda5cac.json"
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

#url = 'http://13.48.149.61:8000/notify.json'
url = 'http://13.48.149.61:8000/notifycache.json'

get_mac = lambda a: a['notifications'][0]['deviceId']
get_coor = lambda a: a['notifications'][0]['geoCoordinate']
get_map = lambda a: a['notifications'][0]['locationMapHierarchy']


# db.child('mp').child('durmac').set({'x':str(1.06), 'y':str(1.03)})


while True:
    time.sleep(1)
    r = requests.get(url)
    a = False
    try:
        a = json.loads('[' + r.text[:-2] + ']')
    except Exception as e:
        print('[' + r.text + ']')
        #print("-------------------------------------")
        print(e)
        #print(re.findall(r'\d+',str(e)))
        #print("-------------------------------------")
    if a:
        print("New entries!!")
        for item in a:
            xy = get_coor(item)
            longitude = xy['longitude']
            latitude = xy['latitude']
            if latitude < 59 or latitude > 63 or longitude < 23 or longitude > 26:
                break

            db.child('mac').child(get_mac(item)).set({'map':str(get_map(item)), 'x' : str(longitude), 'y':str(latitude)})


