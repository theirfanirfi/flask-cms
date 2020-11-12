from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import PageForm
from application.BusinessLogic.PageBL import PageBL
from flask_login import login_required

class PagesView(FlaskView):
	title = 'Pages'
	exclude_methods=['redirect_with_form']
	pbl = PageBL()

	def redirect_with_form(self, form):
		pages = self.pbl.get_pages()
		return render_template("cpanel/page.html",title=self.title, form=form, pages=pages)

	@login_required
	def index(self):
		form = PageForm()
		return self.redirect_with_form(form)

	@login_required
	def get(self, id):
		isPage, pageOrException, msg_type = self.pbl.get_page_by_id(id)
		form = PageForm()
		if not isPage:
			flash(pageOrException, msg_type)
			return self.redirect_with_form(form)

		pages = self.pbl.get_pages()
		form.page_title.data = pageOrException.page_title
		form.page_description.data = pageOrException.page_description
		return render_template("cpanel/page_update.html",page=pageOrException,title=self.title, form=form, pages=pages)

	@route("/update/<int:id>", methods=['POST'])
	@login_required
	def update(self, id):
		form = PageForm()
		if form.validate_on_submit():
			isUpdated, message = self.pbl.update_page(form, id)
			if isUpdated:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("PagesView:index"))
		else:
			return self.redirect_with_form(form)

	@login_required
	def post(self):
		form = PageForm()
		if form.validate_on_submit():
			isSaved, message = self.pbl.add_page(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("PagesView:index"))
		else:
			return self.redirect_with_form(form)

	@route("/delete/<int:id>")
	@login_required
	def delete(self, id):
		isDeleted, message, message_type = self.pbl.delete_page(id)
		flash(message, message_type)
		return redirect(url_for("PagesView:index"))
		