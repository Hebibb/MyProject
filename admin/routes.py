from run import app,db
from flask import render_template,redirect,url_for,request
from modules import *
import datetime
import os


@app.route("/admin",methods=['GET','POST'],)
def admin_index():
   return render_template('admin/base.html')


@app.route("/admin/contact",methods=['GET','POST'])
def contact():
    from modules import Contact
    from run import db
    import datetime
    messages = Contact.query.all()
    if request.method=='POST':
        _ad=request.form['ad']
        _soyad=request.form['soyad']
        _telefon=request.form['telefon']
        _email=request.form['email']
        _message=request.form['message']
        _date=datetime.date.today()
        contact=Contact(
            _ad=_ad,
            _soyad=_soyad,
            _telefon=_telefon,
            _email=_email,
            _message=_message,
            _date=_date
        )   
        db.session.add(contact)
        db.session.commit()
        return redirect('/')
    return render_template('admin/contact.html',messages=messages)

@app.route("/admin/Skills",methods=['GET','POST'])
def my_skills():
    from modules import Skills
    from run import db
    skills = Skills.query.all()
    # Gozde
    if request.method=='POST':
        _icon=request.form['icon']
        _title=request.form['title']
        _desc=request.form['describtion']
        skill=Skills(
            _icon=_icon,
            _title=_title,
            _describtion=_desc 
        )
        
        db.session.add(skill)
        db.session.commit()
        return redirect('/admin')
    
    return render_template('admin/Skills.html',skills=skills)
    
@app.route("/admin/Ourteam",methods=['GET','POST'])
def our_team():
    from modules import Ourteam
    from run import db
    import os
    from werkzeug.utils import secure_filename
    myteam=Ourteam.query.all()
    if request.method=='POST':
        file=request.files['filem']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        _fileAdi=filename
        _fullname=request.form['fullname']
        _profession=request.form['profession']
        team=Ourteam(
            _fileAdi=filename,
            _fullname=_fullname,
            _profession=_profession
            
        )
        db.session.add(team)
        db.session.commit()
        return redirect('/admin/Ourteam')
    
    return render_template('admin/Ourteam.html',myteam=myteam)
 
@app.route("/admin/GetInTouch",methods=['GET','POST'])
def Get_In_T():
    from modules import GetITouch
    from run import db
    elaqe=GetITouch.query.all()
    # Gozde
    if request.method=='POST':
        _ikonam=request.form['ikona']
        _title=request.form['title']
        _cityAdd=request.form['City_Add']
        _countryAdd=request.form['Country_Add']
        
        GIT=GetITouch(
            _ikonam=_ikonam,
            _title=_title,
            _cityAdd=_cityAdd,
            _countryAdd=_countryAdd 
        )
        
        db.session.add(GIT)
        db.session.commit()
        return redirect('/admin/GetInTouch')
    
    return render_template('admin/GetIntouch.html',elaqe=elaqe)    
    
    
    
    
   




