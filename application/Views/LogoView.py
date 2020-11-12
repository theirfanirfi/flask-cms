from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import LogoForm
from application.BusinessLogic.LogoBL import LogoBL
from flask_login import login_required

class LogoView(FlaskView):
	title = 'Logos'
	exclude_methods=['redirect_with_form']
	bl = LogoBL()

	def redirect_with_form(self, form):
		logos = self.bl.get_logos()
		return render_template("cpanel/logo.html",title=self.title, form=form, logos=logos)

	@login_required
	def index(self):
		form = LogoForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass
	@login_required
	def post(self):
		form = LogoForm()
		if form.validate_on_submit():
			isSaved, message = self.bl.add_logo(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("LogoView:index"))
		else:
			return self.redirect_with_form(form)

	@route("/delete/<int:id>")
	@login_required
	def delete(self, id):
		isDeleted, message, message_type = self.bl.delete_logo(id)
		flash(message, message_type)
		return redirect(url_for("LogoView:index"))
		