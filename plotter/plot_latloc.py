import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pyrebase
import time
import random

config = {
"apiKey": "AIzaSyBra07LSvzKcKiicYI32rINLsva8Ozf5D4",
"authDomain": "boys-for-junction.firebaseapp.com",  
"databaseURL": "https://boys-for-junction.firebaseio.com", 
"storageBucket": "boys-for-junction.appspot.com",
# "serviceAccount": "../boys-for-junction-firebase-adminsdk-mq573-34deda5c│ac.json"
 }


firebase = pyrebase.initialize_app(config)
db = firebase.database()

mac_meva = "asd"

while True:  
        a = db.child('mac').get().val()
        x = []
        y = []
        if a != None:
            for elem in a:
                print(elem)
                #if elem == mac_meva: print(elem + " és igual que " + mac_meva +"")
                print(a[elem]['x'])
                print(a[elem]['y'])
                #if a[elem]['map'] == "Otaniemi>Väre>1":
                x.append(float(a[elem]['x']))
                y.append(float(a[elem]['y']))
            
            #for i in range(len(x)):
                #plt.scatter(y[i], x[i], color='red')
            ax=plt.gca()
            ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.25))
            plt.scatter(y,x)
            plt.pause(0.1)
            plt.clf()
        else:
            time.sleep(1)
            print("No data yet")
    #plt.show()

