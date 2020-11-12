from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import PartnerForm
from application.BusinessLogic.PartnerBL import PartnerBL
from flask_login import login_required

class PartnerView(FlaskView):
	title = 'Partners'
	exclude_methods=['redirect_with_form']
	pbl = PartnerBL()

	def redirect_with_form(self, form):
		partners = self.pbl.get_partners()
		return render_template("cpanel/partner.html",title=self.title, form=form, partners=partners)

	@login_required
	def index(self):
		form = PartnerForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass

	@login_required
	def post(self):
		form = PartnerForm()
		if form.validate_on_submit():
			isSaved, message = self.pbl.add_partner(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("PartnerView:index"))
		else:
			return self.redirect_with_form(form)

	@route("/delete/<int:id>")
	@login_required
	def delete(self, id):
		isDeleted, message, message_type = self.pbl.delete_partner(id)
		flash(message, message_type)
		return redirect(url_for("PartnerView:index"))
		