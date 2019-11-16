from flask import Flask, escape, url_for
import json
import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import time

url = 'http://13.48.149.61:8000/notify.json'
app = Flask(__name__)

r = requests.get(url)


get_mac = lambda a: a['notifications'][0]['deviceId']
get_coor = lambda a: a['notifications'][0]['locationCoordinate']
get_map = lambda a: a['notifications'][0]['locationMapHierarchy']
'''with open('/home/horno/hackathons/junction/wifi_stuff/OneDrive_1_11-15-2019/wifidata/notify.json.2019-11-04-16-54', 'r') as fd:
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


for i in range(1000):
    print(i)
    time.sleep(1)


@app.route('/<mac>/')
def user(mac):
    x = json.loads(r.text)
    print("something")
    return "HOTAL"
