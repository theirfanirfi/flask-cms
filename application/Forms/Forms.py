from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField, FileField, FloatField, \
    BooleanField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField()

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField()

class CategoriesForm(FlaskForm):
    cat_title = StringField('Category Title', validators=[DataRequired()])
    product_category = BooleanField('Product Category')
    service_category = BooleanField('Service Category')
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()


class ProductForm(FlaskForm):
    product_title = StringField('Product Title', validators=[DataRequired()])
    product_description = TextAreaField('Product Description', validators=[DataRequired()])
    product_category = SelectField('Select Product Category', choices=[], coerce=str)
    product_image = FileField('Product Image', validators=[
        FileAllowed(['png', 'jpg', 'jpeg'], "JPG, PNG, JPEG files are only allowed.")])
    product_price = FloatField('Product Price', validators=[DataRequired()])
    submit = SubmitField()


class ServiceForm(FlaskForm):
    service_title = StringField('Service Title', validators=[DataRequired()])
    service_description = TextAreaField('Service Description', validators=[DataRequired()])
    service_category = SelectField('Select Service Category', choices=[], coerce=str)
    service_image = FileField('Service Image', validators=[])
    service_price = FloatField('Service Charges', validators=[DataRequired()])
    submit = SubmitField()


class PartnerForm(FlaskForm):
    partner_title = StringField('Partner name', validators=[DataRequired()])
    partner_image = FileField('Partner Image', validators=[])
    submit = SubmitField()


class CustomerForm(FlaskForm):
    customer_name = StringField('Customer name', validators=[DataRequired()])
    customer_image = FileField('Customer Image', validators=[])
    customer_review = TextAreaField('Customer Review', validators=[DataRequired()])
    submit = SubmitField()


class LogoForm(FlaskForm):
    logo_image = FileField('Logo Image', validators=[])
    submit = SubmitField()


class SliderForm(FlaskForm):
    slider_title = StringField('Slider title', validators=[DataRequired()])
    slider_image = FileField('Slider Image', validators=[])
    submit = SubmitField()


class PageForm(FlaskForm):
    page_title = StringField('Page title', validators=[DataRequired()])
    page_description = TextAreaField('Page Description', validators=[DataRequired()])
    submit = SubmitField()
