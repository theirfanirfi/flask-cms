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
from application.Views.ServiceView import ServiceView
from application.Views.PartnerView import PartnerView
from application.Views.SliderView import SliderView
from application.Views.CustomerView import CustomerView
from application.Views.LogoView import LogoView
from application.Views.PageView import PagesView
from application.Views.ProductsView import ProductsView
from application.Views.UserView import UserView
from application.Views.LinksView import LinksView
from application.Views.frontend.FrontEndView import FrontEndView

CategoriesView.register(app, route_base='cpanel/categories/')
ServiceView.register(app, route_base='cpanel/services/')
PartnerView.register(app, route_base='cpanel/partners/')
CustomerView.register(app, route_base='cpanel/customers/')
LogoView.register(app, route_base='cpanel/logos/')
SliderView.register(app, route_base='cpanel/sliders/')
PagesView.register(app, route_base='cpanel/pages/')
ProductsView.register(app, route_base='cpanel/products/')
LinksView.register(app, route_base='cpanel/links/')
UserView.register(app, route_base='/cpanel/login/')
FrontEndView.register(app, route_base='/')


