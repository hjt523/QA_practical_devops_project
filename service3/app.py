from flask import Flask, redirect, render_template, request,url_for 
import random
app = Flask(__name__)

@app.route("/service3", methods =["GET","POST"])
def subject():
    sublist = open("subjects.txt","r")
    subjectlist = sublist.readlines()
    return random.choice(subjectlist)

if __name__=='__main__':
    app.run(host = "0.0.0.0",port=5000, debug=True)