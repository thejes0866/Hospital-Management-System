from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "HMS.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 's@chin002'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth  
    if not path.exists("instance\\HMS.db"):
        with app.app_context():
            from .models import User, Doctor, PatientComments, AppointmentBooking
            db.create_all()
            print('Created Database!')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
 
    return app


