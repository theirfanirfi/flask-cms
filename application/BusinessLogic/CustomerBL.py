from application import db
from application.Models.models import Customer
from application.utils import save_file, delete_image
class CustomerBL:
    def add_customer(self, form):
        customer = Customer()
        customer.customer_name = form.customer_name.data
        customer.customer_review = form.customer_review.data
        isSaved, file_name = save_file(form.customer_image.data, 'customers')
        customer.customer_image = file_name
        try:
            db.session.add(customer)
            db.session.commit()
            return True, 'Customer added.'
        except Exception as e:
            return False, str(e)

    def get_customers(self):
        customers = Customer.query.all()
        return customers

    def delete_customer(self, id):
        customer = Customer.query.filter_by(customer_id=id)
        if not customer.count() > 0:
            return False, 'No such customer found', 'error'

        customer = customer.first()
        delete_image(customer.customer_image,'customers')
        try:
            db.session.delete(customer)
            db.session.commit()
            return True, 'customer deleted', 'success'
        except Exception as e:
            return False, str(e), 'error'
