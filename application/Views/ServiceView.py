from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import ServiceForm
from application.BusinessLogic.ServiceBL import ServiceBL
from flask_login import login_required

class ServiceView(FlaskView):
	title = 'Services'
	exclude_methods=['redirect_with_form']
	sbl = ServiceBL()

	def redirect_with_form(self, form):
		services = self.sbl.get_services()
		form.service_category.choices = self.sbl.get_service_categories()
		return render_template("cpanel/service.html",title=self.title, form=form, services=services)

	@login_required
	def index(self):
		form = ServiceForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass

	@login_required
	def post(self):
		form = ServiceForm()
		form.service_category.choices = self.sbl.get_service_categories()
		if form.validate_on_submit():
			isSaved, message = self.sbl.add_service(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("ServiceView:index"))
		else:
			return self.redirect_with_form(form)

	@route("/delete/<int:id>")
	@login_required
	def delete(self, id):
		isDeleted, message, message_type = self.sbl.delete_service(id)
		flash(message, message_type)
		return redirect(url_for("ServiceView:index"))
		