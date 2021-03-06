from flask import Flask, redirect, render_template, request,url_for 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests
from os import getenv

app = Flask(__name__) # Creating Flask Object
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@34.105.178.235/prior'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = ""

db = SQLAlchemy(app) # create SQLALchemy object
class prior(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doodle = db.Column(db.String(60),nullable=False)

db.create_all()

@app.route("/", methods =["GET","POST"]) # main Page
def main():
    doodle = ""
    doodlesprior = prior.query.order_by(desc(prior.id)).limit(5).all()
    #if request.method == "POST" :
    aes = requests.get("http://doodlestack_service2:5000/service2").text
    
    sub = requests.get("http://doodlestack_service3:5000/service3").text
    
    doodle = requests.post("http://doodlestack_service4:5000/service4", data= aes + "_"+sub).text
    
    

    storedoodle = prior(doodle = doodle)
    db.session.add(storedoodle)
    db.session.commit()
    
    return render_template("main.html", doodle = doodle , doodlesprior = doodlesprior)
    #return render_template("main.html", doodle = doodle)



if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)


