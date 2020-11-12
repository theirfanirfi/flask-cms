from application import db
from application.Models.models import Slider
from application.utils import save_file, delete_image
class SliderBL:
    def add_slider(self, form):
        slider = Slider()
        slider.slider_title = form.slider_title.data
        isSaved, file_name = save_file(form.slider_image.data, 'sliders')
        slider.slider_image = file_name
        try:
            db.session.add(slider)
            db.session.commit()
            return True, 'Slider added.'
        except Exception as e:
            return False, str(e)

    def get_sliders(self):
        sliders = Slider.query.all()
        return sliders


    def delete_slider(self, id):
        slider = Slider.query.filter_by(slider_id=id)
        if not slider.count() > 0:
            return False, 'No such slider found', 'error'

        slider = slider.first()
        delete_image(slider.slider_image,'sliders')
        try:
            db.session.delete(slider)
            db.session.commit()
            return True, 'slider deleted', 'success'
        except Exception as e:
            return False, str(e), 'error'