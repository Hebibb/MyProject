from run import app
from flask import render_template


@app.route("/admin",methods=['GET','POST'],)
def admin_index():
   return render_template('admin/index.html')

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





