from run import db

class Skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    _title=db.Column(db.String(20))
    _describtion=db.Column(db.String(250))
    
