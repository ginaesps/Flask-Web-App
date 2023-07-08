#this will make the folder a python package
# anything coded in here will be accessible from the outside

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "flaskwebapp.db"

def create_app(): 
    #__name__ represents the name of the file or file that was ran
    app = Flask(__name__)
    # the secret key encodes the cookies and session data
    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    # url_prefix indicates if the routes need a prev direction so you can access them
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')