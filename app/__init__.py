from flask import Flask
from flask_login import LoginManager
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine
import json


with open('config.json', 'r') as f:
    config = json.load(f)
    database_uri = config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
Base=declarative_base()
app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import Base, User
Base.metadata.create_all(engine)

@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user = session.query(User).get(int(user_id))
    session.close()
    return user

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .books import app as name_blueprint
app.register_blueprint(name_blueprint)