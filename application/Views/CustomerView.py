from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import CustomerForm
from application.BusinessLogic.CustomerBL import CustomerBL
from flask_login import login_required


class CustomerView(FlaskView):
	title = "Customers' Reviews"
	exclude_methods=['redirect_with_form']
	cbl = CustomerBL()

	def redirect_with_form(self, form):
		customers = self.cbl.get_customers()
		return render_template("cpanel/customer.html",title=self.title, form=form, customers=customers)

	@login_required
	def index(self):
		form = CustomerForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass
	@login_required
	def post(self):
		form = CustomerForm()
		if form.validate_on_submit():
			isSaved, message = self.cbl.add_customer(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("CustomerView:index"))
		else:
			return self.redirect_with_form(form)

	@route("/delete/<int:id>")
	@login_required
	def delete(self, id):
		isDeleted, message, message_type = self.cbl.delete_customer(id)
		flash(message, message_type)
		return redirect(url_for("CustomerView:index"))
		