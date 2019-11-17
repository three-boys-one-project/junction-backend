from flask import Flask, escape, url_for
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pyrebase
import json
import time
import random
import threading

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

@app.route('/<mac>/')
def get_info(mac):
    tmp = db.child('places').get().val()
    a = list(tmp)
    key = a.pop(random.randint(0, len(a) - 1))
    if random.randint(1,101) < 80:
        return json.dumps({"response":"Nothing to see here"})
    return json.dumps({"response":str(tmp[key]['message'])})

'''@app.route('/init/')
def init_routine():
    #try:
    threading.Thread(target=find_matches).start()
    #except:
        #print("Error in the creation of threads")
    return "Done!"


def find_matches():
    for elems in db.child('mac').get().val():
        print(elems)
    print("Done too!")
    return "Done!"
'''
@app.route('/mac/<mac_a_trobar>/')
def user(mac_a_trobar):
    #x = json.loads(r.text)
    print("Mac a trobar = " + mac_a_trobar)
    n_macs = 0
    trobada = False
    tosend = {}
    tosend["response"] = "Nothing to see here"
    try:
        if mac_a_trobar != "favicon.ico":
            a = db.get().val()
            for elem in a:
                for mac in a[elem]:
                    n_macs = n_macs + 1
                    if mac == mac_a_trobar:
                        trobada = True
                        print(mac + " trobat!")
                    else:
                        print(mac + " no concorda amb " + mac_a_trobar)

        if trobada: print("trobada bro")
        print(n_macs)
        return a
    except Exception as _:
        return '{"response":"KO"}'

















