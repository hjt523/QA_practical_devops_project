from flask import Flask, redirect, render_template, request,url_for 
import random
app = Flask(__name__)

@app.route("/service2", methods =["GET","POST"])
def aesthetic():
    aeslist = open("aesthetics.txt","r")
    aestheticlist = aeslist.readlines()
    return random.choice(aestheticlist)


if __name__=='__main__':
    app.run(host = "0.0.0.0",port=5000, debug=True)