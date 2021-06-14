
from flask import Flask, redirect, render_template, request,url_for 
import random
import requests
app = Flask(__name__)

@app.route("/service4", methods =["GET","POST"])
def doodle():
    
    incstring = request.data.decode('utf-8')
    pair = incstring.split("_")
    aesthetic = pair[0]
    subject = pair[1]

    if len(aesthetic) >= len(subject):
        terlist = open("terrain.txt","r")
        terrainlist = terlist.readlines()
        secondary = random.choice(terrainlist)
        doodle = " A "+ aesthetic + " "+ subject+ " devours the "+ secondary
        return doodle
    else:
        terlist = open("terrain.txt","r")
        terrainlist = terlist.readlines()
        secondary = random.choice(terrainlist)
        doodle = " A "+ aesthetic+" " +secondary + " consumed by many "+ subject+"'s"
        return doodle

if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)
