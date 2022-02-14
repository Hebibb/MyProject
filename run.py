from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

   
from admin.routes import *
from app.routes import *

if __name__ == '__main__':
    # db.create_all()
    app.run(port=5000,debug=True)
