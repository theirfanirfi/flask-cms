from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import FooterContactForm
from application.BusinessLogic.SettingsBL import SettingsBL
from flask_login import login_required

class SettingsView(FlaskView):
	title = 'Footer Contact Us Description'
	exclude_methods=['redirect_with_form']
	bl = SettingsBL()

	def redirect_with_form(self, form):
		isAvailable, footer = self.bl.get_footerSettingObject()
		if isAvailable:
			form.setting_description.data = footer.setting_description


		return render_template("cpanel/footer_contact.html",title=self.title, form=form)

	@login_required
	def index(self):
		form = FooterContactForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass

	@login_required
	def post(self):
		form = FooterContactForm()
		if form.validate_on_submit():
			isSaved, message = self.bl.addOrUpdateSetting(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("SettingsView:index"))
		else:
			return self.redirect_with_form(form)
		