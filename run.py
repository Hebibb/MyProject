from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
# db = SQLAlchemy(app)
# class Skills(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     ad_soyad=db.Column(db.String(40))
#     telefon=db.Column(db.String(10))
#     email=db.Column(db.String(20))
#     message=db.Column(db.String(200))
#     ad_soyad=db.Column(db.String(50))
    
# db.create_all()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skills.db'
db = SQLAlchemy(app)
class skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    _title=db.Column(db.String(20))
    _describtion=db.Column(db.String(250))
   
    
db.create_all()

from admin.routes import *
from app.routes import *



if __name__ == '__main__':
 
    app.run(port=5000,debug=True)
