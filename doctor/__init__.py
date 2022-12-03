from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doctor.db' #File that will be recognized as database
app.config['SECRET_KEY'] = 'e20d78b21c8345a7be45d8c8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view="login_page" #redirect when we need to log in
login_manager.login_message_category="info"
