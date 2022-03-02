from run import db
from flask_login.mixins import UserMixin

class Skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    _icon=db.Column(db.String(40))
    _title=db.Column(db.String(20))
    _describtion=db.Column(db.String(250))
    
class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    _ad=db.Column(db.String(20))
    _soyad=db.Column(db.String(20))
    _telefon=db.Column(db.String(20))
    _email=db.Column(db.String(50))
    _message=db.Column(db.String(250))
    _date=db.Column(db.String(20))
    
class Ourteam(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    _fullname=db.Column(db.String(50))
    _profession=db.Column(db.String(50))
    _fileAdi=db.Column(db.String(50))
class GetITouch(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    _ikonam=db.Column(db.String(40))
    _title=db.Column(db.String(20))
    _cityAdd=db.Column(db.String(100))
    _countryAdd=db.Column(db.String(100))
class Blogs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blogger=db.Column(db.String(50))
    blog_pic=db.Column(db.String(50))
    blog_title=db.Column(db.String(20))
    blog_cont=db.Column(db.String(150))
    blog_url=db.Column(db.String(80))
    comment_date=db.Column(db.String(80))
class Feedback(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    feeder_pic=db.Column(db.String(30))
    _name=db.Column(db.String(30))
    _city=db.Column(db.String(50))
    _assessment=db.Column(db.String(30))
    feed_date=db.Column(db.String(30))

# Login
class Login(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)

    
