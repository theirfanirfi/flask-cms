from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for, request
from application.Forms.Forms import UserForm, LoginForm, ChangePasswordForm
from application.BusinessLogic.UserBL import UserBL
from application.BusinessLogic.SMLinksBL import SMLinksBL
from application.BusinessLogic.CustomerBL import CustomerBL
from application.BusinessLogic.PageBL import PageBL
from flask_login import login_user, logout_user, login_required, current_user
from application.Models.models import Logo, Slider, Pages, Partner, Product, Service, Categories, Customer


class FrontEndView(FlaskView):
	title = 'Login'
	exclude_methods=['redirect_with_form']
	ubl = UserBL()
	linksBL = SMLinksBL()
	cbl = CustomerBL()
	pbl = PageBL()

	def redirect_with_details(self, template, data):
		pages = Pages.query.all()
		logo = Logo.query.first()
		links = self.linksBL.get_links_for_frontend()
		service_categories = Categories.query.filter_by(service_category=1).all()
		product_categories = Categories.query.filter_by(product_category=1).all()
		return render_template(template,title=self.title,service_categories=service_categories,
							   product_categories=product_categories,pages=pages, logo=logo,
							   links=links, data=data)

	def index(self):
		sliders = Slider.query.all()
		customers = self.cbl.get_customers()
		partners = Partner.query.all()
		products = Product.query.all()
		services = Service.query.all()
		contact = self.pbl.get_contact_page_for_frontend_link()

		data = {
			'sliders': sliders,
			'customers': customers,
			'partners': partners,
			'products': products,
			'services': services,
			'contact': contact,
		}
		return self.redirect_with_details("frontend/home.html", data)

	def products(self):
		products = Product.query.all()
		categoires = Categories.query.filter_by(product_category=1).all()
		data = {
			'products' : products,
			'categories': categoires
		}
		return self.redirect_with_details("frontend/products.html",data)


	def product(self, id):
		product = Product.query.filter_by(product_id=id)
		if not product.count()>0:
			return 'page not found'
		product = product.first()
		categoires = Categories.query.filter_by(product_category=1).all()
		data = {
			'product':product,
			'categories': categoires
		}
		return self.redirect_with_details("frontend/product.html", data)

	def services(self):
		services = Service.query.all()
		categoires = Categories.query.filter_by(product_category=1).all()
		data = {
			'services' : services,
			'categories': categoires
		}
		return self.redirect_with_details("frontend/services.html",data)


	def service(self, id):
		service = Service.query.filter_by(service_id=id)
		if not service.count()>0:
			return 'page not found'
		service = service.first()
		categoires = Categories.query.filter_by(product_category=1).all()
		data = {
			'service':service,
			'categories': categoires
		}
		return self.redirect_with_details("frontend/service.html", data)

	def products_by_category(self, id):
		products = Product.query.filter_by(product_category=id).all()
		categoires = Categories.query.filter_by(product_category=1).all()
		data = {
			'products' : products,
			'categories': categoires
		}
		return self.redirect_with_details("frontend/products.html",data)

	def services_by_category(self, id):
		services = Service.query.filter_by(service_category=id).all()
		categoires = Categories.query.filter_by(service_category=1).all()
		data = {
			'services' : services,
			'categories': categoires
		}
		return self.redirect_with_details("frontend/services.html",data)

	@route("/search", methods=['POST'])
	def search(self):
		search_term = request.form['search_term']
		search_term = "%{}%".format(search_term)
		products = Product.query.filter(Product.product_title.like(search_term)).all()
		services = Service.query.filter(Service.service_title.like(search_term)).all()
		data = {
			'products': products,
			'services':services
		}
		return self.redirect_with_details("frontend/search.html", data)

	def page(self, id):
		page = Pages.query.filter_by(page_id=id)
		if not page.count() > 0:
			return 'Invalid request'
		page = page.first()
		data = {'page': page}
		return self.redirect_with_details("frontend/page.html", data)

	def partners(self):
		partners = Partner.query.all()
		data = {'partners': partners}
		return self.redirect_with_details("frontend/partner.html", data)

	def customers(self):
		customers = Customer.query.all()
		data = {'customers': customers}
		return self.redirect_with_details("frontend/our_customers.html", data)
		