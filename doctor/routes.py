from doctor import app
from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from doctor.login import User
from doctor.forms import LoginForm
from doctor import db
from flask_login import login_user,logout_user,login_required,current_user