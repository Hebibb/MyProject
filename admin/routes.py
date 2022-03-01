from run import app,db
from flask import render_template,redirect,url_for,request
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager
from modules import *
import datetime
import os

# Login
@login_manager.user_loader
def load_user(user_id):
    from modules import Login
    return Login.query.get(int(user_id))

@app.route("/login", methods = ["GET","POST"])
def admin_login():
    from modules import Login
    from run import db
    login = Login (
        admin_username = "Habib",
        admin_password = "Habib95",
        log_bool = False
    )
    db.session.add(login)
    db.session.commit()
    
    if request.method == "POST":
        if login.admin_username == request.form["admin_username"] and login.admin_password == request.form["admin_password"]:
            login_user(login, remember=login.log_bool)
            return redirect(url_for("admin_index"))
        else:
            return redirect(url_for("admin_login"))
    return render_template("admin/login.html", login = login)

# Logout
@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for("app_index"))

@app.route("/admin",methods=['GET','POST'],)
@login_required
def admin_index():
   return render_template('admin/base.html')


@app.route("/admin/contact",methods=['GET','POST'])
@login_required
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
@login_required
def my_skills():
    from modules import Skills
    from run import db
    skills = Skills.query.all()

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
    
@app.route("/SkillDelete/<int:id>",methods=["GET","POST"])
@login_required
def Skill_delete(id):
    from modules import Skills
 
    from run import db
    skl = Skills.query.filter_by(id=id).first()
    db.session.delete(skl)
    db.session.commit()
    return redirect ("/admin")
    



@app.route("/admin/Blog",methods=['GET','POST'])
@login_required
def _blogin():
    from modules import Blogs
    from run import db
    myblog = Blogs.query.all()
  
    if request.method=='POST':
        import datetime
        file=request.files['bl_img']
        filename = file.filename
        file.save(os.path.join('static/uploads/',filename))
        blog_title=request.form['bl_title']
        blog_cont=request.form['bl_content']
        blog_url=request.form['bl_url']
        blogger=request.form['blogger']
        comment_date=datetime.date.today()
     
        
       
        blog=Blogs(
            blog_pic=filename,
            blog_title=blog_title,
            blog_cont=blog_cont,
            blog_url=blog_url,
            blogger=blogger,
            comment_date=comment_date
        )
        
        db.session.add(blog)
        db.session.commit()
        return redirect('/admin/Blog')
    
    return render_template('admin/Blog.html',myblog=myblog)


@app.route("/blogDelete/<int:id>",methods=["GET","POST"])
@login_required
def blog_delete(id):
    from modules import Blogs
    from run import db
    myblog = Blogs.query.filter_by(id=id).first()
    db.session.delete(myblog)
    db.session.commit()
    return redirect ("/admin/Blog")


@app.route("/blogEdit/<int:id>",methods=["GET","POST"])
@login_required
def blog_edit(id):
    from modules import Blogs
    from run import db
    newblog = Ourteam.query.filter_by(id=id).first()
    if request.method=="POST":
        new_bl = Blogs.query.filter_by(id=id).first()
    
        new_bl.blog_title = request.form["bl_title"]
        new_bl.blog_cont=request.form["bl_content"]
        blog_url=request.form["bl_url"]
        
        
        db.session.commit()
        return redirect("/admin/Blog")
    return render_template ("/admin/updBlog.html",newblog=newblog)

















 
@app.route("/admin/GetInTouch",methods=['GET','POST'])
@login_required
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
    
@app.route("/GITDelete/<int:id>",methods=["GET","POST"])
@login_required
def GIT_delete(id):
    from modules import GetITouch
    from run import db
    getit = GetITouch.query.filter_by(id=id).first()
    db.session.delete(getit)
    db.session.commit()
    return redirect ("/admin/GetInTouch")
    
    
    
   
@app.route("/GITEdit/<int:id>",methods=["GET","POST"])
@login_required
def GIT_edit(id):
    from modules import GetITouch
    from run import db
    newGIT = GetITouch.query.filter_by(id=id).first()
    if request.method=="POST":
        getit = GetITouch.query.filter_by(id=id).first()
        getit._ikonam=request.form["ikona"]   
        getit._title=request.form["title"]
        getit._cityAdd=request.form["City_Add"]
        getit._countryAdd=request.form["Country_Add"]
        db.session.commit()
        return redirect("/admin/GetInTouch")
    return render_template ("/admin/updateGIT.html",newGIT=newGIT)    






    
    
@app.route("/admin/Ourteam",methods=['GET','POST'])
@login_required
def our_team():
    from modules import Ourteam
    from run import db
    import os
    from werkzeug.utils import secure_filename
    myteam=Ourteam.query.all()
    if request.method=='POST':
        file=request.files['filem']
        filename = file.filename
        file.save(os.path.join('static/uploads/',filename))
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
 
@app.route("/memberDelete/<int:id>",methods=["GET","POST"])
@login_required
def team_delete(id):
    from modules import Ourteam
    from run import db
    myteam = Ourteam.query.filter_by(id=id).first()
    db.session.delete(myteam)
    db.session.commit()
    return redirect ("/admin/Ourteam")


@app.route("/memberEdit/<int:id>",methods=["GET","POST"])
@login_required
def team_edit(id):
    from modules import Ourteam
    from run import db
    newMember = Ourteam.query.filter_by(id=id).first()
    if request.method=="POST":
        Member = Ourteam.query.filter_by(id=id).first()
        Member._fileAdi = request.form["filem"]   
        Member._fullname = request.form["fullname"]
        Member._profession=request.form["profession"]
        db.session.commit()
        return redirect("/admin/Ourteam")
    return render_template ("/admin/updTeam.html",newMember=newMember)
 
 
 
 

