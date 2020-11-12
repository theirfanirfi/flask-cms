from application import db
from application.Models.models import Logo
from application.utils import save_file, delete_image
class LogoBL:
    def add_logo(self, form):
        logo = Logo()
        isSaved, file_name = save_file(form.logo_image.data, 'logos')
        logo.logo_image = file_name
        try:
            db.session.add(logo)
            db.session.commit()
            return True, 'Logo added.'
        except Exception as e:
            return False, str(e)

    def get_logos(self):
        logos = Logo.query.all()
        return logos

    def delete_logo(self, id):
        logo = Logo.query.filter_by(logo_id=id)
        if not logo.count() > 0:
            return False, 'No such logo found', 'error'

        logo = logo.first()
        delete_image(logo.logo_image,'logos')
        try:
            db.session.delete(logo)
            db.session.commit()
            return True, 'logo deleted', 'success'
        except Exception as e:
            return False, str(e), 'error'