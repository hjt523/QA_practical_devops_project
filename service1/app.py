from flask import Flask, redirect, render_template, request,url_for 
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__) # Creating Flask Object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = ""

db = SQLAlchemy(app) # create SQLALchemy object

@app.route("/", methods =["GET","POST"]) # main Page
def main():
    #doodle = "Example output"
    #if request.method == "POST" :
    aes = requests.get("http://service2:5000/service2").text
    print(aes)
    sub = requests.get("http://service3:5000/service3").text
    
    doodle = requests.post("http://service4:5000/service4", data= aes + "_"+sub).text
    print (doodle)
    return render_template("main.html", doodle = doodle )
    #return render_template("main.html", doodle = doodle)

if __name__=='__main__':
    app.run(host = "0.0.0.0",port=5000, debug=True)


