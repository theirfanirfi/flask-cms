from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from application.config import Config
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()


app = Flask(__name__)
app.config.from_object(Config)

app.jinja_env.filters['str'] = str()
db.app = app
db.init_app(app)
bcrypt.init_app(app)



migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'UserView:index'
login_manager.login_message_category = 'info'

from application.Models import *

# from application.cpanel.routes import cpanel

# # # app.register_blueprint(main)
# # app.register_blueprint(cpanel, url_prefix="/cpanel")

from application.Views.CategoriesView import CategoriesView
from application.Views.PostsView import PostsView
from application.Views.UserView import UserView
#
#
# ProductsView.register(app, route_base='cpanel/products/')
UserView.register(app, route_base='/cpanel/login/')
PostsView.register(app, route_base='/cpanel/posts/')
CategoriesView.register(app, route_base='/cpanel/categories/')


