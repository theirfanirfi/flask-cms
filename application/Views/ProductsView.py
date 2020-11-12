from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import ProductForm
from application.BusinessLogic.ProductsBL import ProductsBL
from flask_login import login_required

class ProductsView(FlaskView):
	title = 'Products'
	exclude_methods=['redirect_with_form']
	pbl = ProductsBL()

	def redirect_with_form(self, form):
		products = self.pbl.get_products()
		form.product_category.choices = self.pbl.get_product_categories()
		return render_template("cpanel/product.html",title=self.title, form=form, products=products)

	@login_required
	def index(self):
		form = ProductForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass

	@login_required
	def post(self):
		form = ProductForm()
		form.product_category.choices = self.pbl.get_product_categories()
		if form.validate_on_submit():
			isSaved, message = self.pbl.add_product(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("ProductsView:index"))
		else:
			return self.redirect_with_form(form)

	@route("/delete/<int:id>")
	@login_required
	def delete(self, id):
		isDeleted, message, message_type = self.pbl.delete_product(id)
		flash(message, message_type)
		return redirect(url_for("ProductsView:index"))
		