from run import app
from flask import render_template
from modules import *
from admin.routes import *



@app.route("/",methods=['GET','POST'])
def app_index():
    from modules import Skills
    from modules import Contact
    from modules import Ourteam
    from modules import GetITouch
    from modules import Blogs
    from modules import Feedback
    
    messages=Contact.query.all()
    skills=Skills.query.all()
    myteam=Ourteam.query.all()
    elaqe=GetITouch.query.all()
    myblog = Blogs.query.all()
    feedb = Feedback.query.all()
    
    return render_template('app/index.html',skills=skills,messages=messages,myteam=myteam,elaqe=elaqe,myblog=myblog,feedb=feedb)







