from run import app,db
from flask import render_template,redirect,url_for,request
from modules import *


@app.route("/admin",methods=['GET','POST'],)
def admin_index():
   return render_template('admin/base.html')

users=[]
@app.route("/admin/contact",methods=['GET','POST'])
def contact():
    if request.method=='POST':
        _ad=request.form['ad ']
        _soyad=request.form['soyad ']
        _telefon=request.form['telefon ']
        _email=request.form['email ']
        _message=request.form['message ']
        _date=datetime.date.today()
        user={
            'ad':_ad,
            'soyad':_soyad,
            'telefon':_telefon,
            'email':_email,
            'message':_message,
            'date':_date
        }
        users.append(user)
        # return redirect('/')

    return render_template('admin/contact.html',istifadeciler=users)

@app.route("/admin/Skills",methods=['GET','POST'])
def my_skills():
    from modules import Skills
    from run import db
    skills = Skills.query.all()
    # Gozde
    if request.method=='POST':
        _title=request.form['title']
        _desc=request.form['describtion']
        skill=Skills(
            _title=_title,
            _describtion=_desc 
        )
        
        db.session.add(skill)
        db.session.commit()
        return redirect('/admin')
    
    return render_template('admin/Skills.html',skills=skills)
    





