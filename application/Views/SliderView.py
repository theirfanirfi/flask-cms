from flask_classful import FlaskView, route
from flask import render_template, flash, redirect, url_for
from application.Forms.Forms import SliderForm
from application.BusinessLogic.SliderBL import SliderBL
from flask_login import login_required


class SliderView(FlaskView):
	title = 'Slider Images'
	exclude_methods=['redirect_with_form']
	sbl = SliderBL()

	def redirect_with_form(self, form):
		sliders = self.sbl.get_sliders()
		return render_template("cpanel/slider.html",title=self.title, form=form, sliders=sliders)

	@login_required
	def index(self):
		form = SliderForm()
		return self.redirect_with_form(form)

	def get(self, id):
		pass
	def put(self, id):
		pass

	@login_required
	def post(self):
		form = SliderForm()
		if form.validate_on_submit():
			isSaved, message = self.sbl.add_slider(form)
			if isSaved:
				flash(message, 'success')
			else:
				flash(message, 'error')
			return redirect(url_for("SliderView:index"))
		else:
			return self.redirect_with_form(form)

	@route("/delete/<int:id>")
	@login_required
	def delete(self, id):
		isDeleted, message, message_type = self.sbl.delete_slider(id)
		flash(message, message_type)
		return redirect(url_for("SliderView:index"))
		