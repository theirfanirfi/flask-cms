from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import SMLinksForm
from application.BusinessLogic.SMLinksBL import SMLinksBL
from flask_login import login_required

class LinksView(FlaskView):
	title = 'Social Media Links'
	exclude_methods=['redirect_with_form']
	bl = SMLinksBL()

	def redirect_with_form(self, form):
		areLinksAvailable, link = self.bl.get_links()
		if areLinksAvailable:
			form.fb_link.data = link.fb_link
			form.twitter_link.data = link.twitter_link
			form.instagram_link.data = link.instagram_link
			form.google_plus_link.data = link.google_plus_link
			form.linkedin_link.data = link.linkedin_link


		return render_template("cpanel/smlinks.html",title=self.title, form=form)

	@login_required
	def index(self):
		form = SMLinksForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass

	@login_required
	def post(self):
		form = SMLinksForm()
		if form.validate_on_submit():
			isSaved, message = self.bl.addOrUpdateLinks(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("LinksView:index"))
		else:
			return self.redirect_with_form(form)
		