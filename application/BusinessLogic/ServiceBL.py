from application import db
from application.Models.models import Service, Categories
from application.utils import save_file, delete_image
class ServiceBL:
    def add_service(self, form):
        service = Service.query.filter_by(service_title=form.service_title.data)
        if service.count() > 0:
            return False, 'Service already exists'
        service = Service()
        service.service_title = form.service_title.data
        service.service_description = form.service_description.data
        service.service_category = form.service_category.data
        service.service_charges = form.service_price.data
        isSaved, file_name = save_file(form.service_image.data, 'services')
        service.service_image = file_name
        try:
            db.session.add(service)
            db.session.commit()
            return True, 'Service added.'
        except Exception as e:
            return False, str(e)

    def get_services(self):
        services = Service.query.all()
        return services

    def get_service_categories(self):
        cats = Categories.query.filter_by(service_category=1).all()
        cats = [(str(c.cat_id), str(c.cat_title)) for c in cats]
        return cats


    def delete_service(self, id):
        service = Service.query.filter_by(service_id=id)
        if not service.count() > 0:
            return False, 'No such service found', 'error'

        service = service.first()
        delete_image(service.service_image,'services')
        try:
            db.session.delete(service)
            db.session.commit()
            return True, 'service deleted', 'success'
        except Exception as e:
            return False, str(e), 'error'