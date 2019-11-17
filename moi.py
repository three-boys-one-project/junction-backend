from flask import Flask, escape, url_for
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pyrebase
import json
import time
import random


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
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
        
    print(x[0])
    print(y[0])

    plt.scatter(x, y)
    plt.show()

    return "Hi and stuff"

@app.route('/<mac>/')
def get_info(mac):
    if random.randint(1,3) % 2:
        return json.dumps({"response":"Nothing to see here"})
    return json.dumps({"response":"Yo should go duck urself, quack!"})


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

