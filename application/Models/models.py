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
	token = db.Column(db.String(200), nullable=True)
	password = db.Column(db.String(200), nullable=False)
	is_admin = db.Column(db.Integer, default=0)


	def get_id(self):
		return (self.user_id)

class Categories(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	cat_title = db.Column(db.String(200), nullable=False)

class Post(db.Model):
	post_id = db.Column(db.Integer, primary_key=True)
	post_title = db.Column(db.String(200), nullable=False)
	post_description = db.Column(db.Text, nullable=True)
	post_image = db.Column(db.Text, nullable=True)
	post_category = db.Column(db.Integer, nullable=True)
	is_admin_post = db.Column(db.Integer, default=0)
	user_id = db.Column(db.Integer, nullable=False)
