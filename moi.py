from flask import Flask, escape, url_for
from collections import defaultdict
import matplotlib.pyplot as plt
import request
import json
import time

config = {
    "apiKey": "AIzaSyBra07LSvzKcKiicYI32rINLsva8Ozf5D4",
    "authDomain": "boys-for-junction.firebaseapp.com",
    "databaseURL": "https://boys-for-junction.firebaseio.com", 
    "storageBucket": "boys-for-junction.appspot.com",
    "serviceAccount": "../boys-for-junction-firebase-adminsdk-mq573-34deda5cac.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)

@app.route('/<mac>/')
def user(mac):
    #x = json.loads(r.text)
    tosend = {}
    tosend["response"] = "Nothing to see here" 

    return json.dumps(tosend, ensure_ascii=False)





'''get_mac = lambda a: a['notifications'][0]['deviceId']
get_coor = lambda a: a['notifications'][0]['locationCoordinate']
get_map = lambda a: a['notifications'][0]['locationMapHierarchy']
with open('/home/horno/hackathons/junction/wifi_stuff/OneDrive_1_11-15-2019/wifidata/notify.json.2019-11-04-16-54', 'r') as fd:
    a = json.load(fd)
dicc = defaultdict(lambda : defaultdict(list))

for noti in a:
    xy = get_coor(noti)
    x = xy['x']
    y = xy['y']
    dicc[get_map(noti)][get_mac(noti)].append((x, y))

# print(dicc)
keys = list(dicc.keys())
macs = list(dicc[keys[0]].keys())
X, Y = list(zip(*dicc[keys[0]][macs[3]]))
plt.scatter(X, Y)
plt.show()
'''
