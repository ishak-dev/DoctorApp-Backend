from doctor import app
from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from doctor.login import User
from doctor.forms import LoginForm
from doctor import db
from flask_login import login_user,logout_user,login_required,current_user




@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Uspjesno ste se logovali: {attempted_user.fullname} ',category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'Pogresan e-mail ili password',category='danger')

    
    return render_template('login.html',form=form)



@app.route('/home',methods=['GET','POST'])
def home_page():
    return render_template('home.html')


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!",category='info')
    return redirect(url_for("login_page"))