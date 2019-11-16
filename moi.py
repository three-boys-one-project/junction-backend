from flask import Flask, escape, url_for
from collections import defaultdict
import matplotlib.pyplot as plt
import pyrebase
import json
import time

config = {
    "apiKey": "AIzaSyBra07LSvzKcKiicYI32rINLsva8Ozf5D4",
    "authDomain": "boys-for-junction.firebaseapp.com",
    "databaseURL": "https://boys-for-junction.firebaseio.com", 
    "storageBucket": "boys-for-junction.appspot.com",
    # "serviceAccount": "../boys-for-junction-firebase-adminsdk-mq573-34deda5cac.json"
}




firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)

places = {'fountain':(24,11), 'terrace':(73,56), 'dancehall':(5,9)}

@app.route('/')
def pro():
    return "Hi and stuff"

@app.route('/places/')
def show_interest_points():
    for elem in places:
        plt.scatter(places[elem][0], places[elem][1])
    plt.show()
    return json.dumps(places, ensure_ascii= True)    

@app.route('/<mac>/')
def get_info(mac):
    return json.dumps({"response":"Ei que tal " + mac})


@app.route('/mac/<mac_a_trobar>/')
def user(mac_a_trobar):
    #x = json.loads(r.text)
    print("Mac a trobar = " + mac_a_trobar)
    n_macs = 0
    trobada = False
    tosend = {}
    tosend["response"] = "Nothing to see here bucko"
    try:
        if mac_a_trobar != "favicon.ico":
            a = db.get().val()
            for elem in a:
                for mac in a[elem]:
                    n_macs = n_macs + 1
                    if mac == mac_a_trobar:
                        trobada = True
                        print(mac + " trobat!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    else:
                        print(mac + " no concorda amb " + mac_a_trobar)

        if trobada: print("trobada bro")
        print(n_macs)
        return a
    except Exception as e:
        return '{"response":"KO"}'

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
