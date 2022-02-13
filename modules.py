from run import db

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
    _ikona=db.Column(db.String(40))
    _title=db.Column(db.String(20))
    _cityAdd=db.Column(db.String(100))
    _countryAdd=db.Column(db.String(100))