from application import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user):
    return User.query.get(user)

class User(db.Model, UserMixin):
	__tablename__ = "users"
	user_id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(100), nullable=False, unique=True)
	password = db.Column(db.String(200), nullable=False)

	def get_id(self):
		return (self.user_id)

class Categories(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	cat_title = db.Column(db.String(200), nullable=False)
	service_category = db.Column(db.Integer, default=0)
	product_category = db.Column(db.Integer, default=0)

class Product(db.Model):
	product_id = db.Column(db.Integer, primary_key=True)
	product_title = db.Column(db.String(200), nullable=False)
	product_description = db.Column(db.Text, nullable=True)
	product_price = db.Column(db.Float, nullable=False)
	product_image = db.Column(db.Text, nullable=True)
	product_category = db.Column(db.Integer, nullable=False)


class Service(db.Model):
	service_id = db.Column(db.Integer, primary_key=True)
	service_title = db.Column(db.String(200), nullable=False)
	service_description = db.Column(db.Text, nullable=True)
	service_charges = db.Column(db.Float, nullable=False)
	service_image = db.Column(db.Text, nullable=True)
	service_category = db.Column(db.Integer, nullable=False)



class Partner(db.Model):
	__tablename__ = "partners"
	partner_id = db.Column(db.Integer, primary_key=True)
	partner_title = db.Column(db.String(200), nullable=False)
	partner_image = db.Column(db.Text, nullable=True)

class Customer(db.Model):
	__tablename__ = "customers"
	customer_id = db.Column(db.Integer, primary_key=True)
	customer_name = db.Column(db.String(200), nullable=False)
	customer_image = db.Column(db.Text, nullable=True)
	customer_review = db.Column(db.Text, nullable=True)

class Logo(db.Model):
	__tablename__ = "logos"
	logo_id = db.Column(db.Integer, primary_key=True)
	logo_image = db.Column(db.Text, nullable=False)

class Slider(db.Model):
	__tablename__ = "sliders"
	slider_id = db.Column(db.Integer, primary_key=True)
	slider_title = db.Column(db.Text, nullable=True)
	slider_image = db.Column(db.Text, nullable=False)

class Pages(db.Model):
	__tablename__ = "pages"
	page_id = db.Column(db.Integer, primary_key=True)
	page_title = db.Column(db.String(100), nullable=False)
	page_description = db.Column(db.Text, nullable=True)

class SMLink(db.Model):
	__tablename__= "social_media_links"
	sm_id = db.Column(db.Integer, primary_key=True)
	fb_link = db.Column(db.String(200), nullable=True)
	twitter_link = db.Column(db.String(200), nullable=True)
	instagram_link = db.Column(db.String(200), nullable=True)
	google_plus_link = db.Column(db.String(200), nullable=True)
	linkedin_link = db.Column(db.String(200), nullable=True)

class Settings(db.Model):
	__tablename__= "settings"
	setting_id = db.Column(db.Integer, primary_key=True)
	setting_type = db.Column(db.String(50), nullable=False)
	setting_description = db.Column(db.Text, nullable=False)
