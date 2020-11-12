from application import db
from application.Models.models import Product, Categories
from application.utils import save_file, delete_image
class ProductsBL:
    def add_product(self, form):
        product = Product.query.filter_by(product_title=form.product_title.data)
        if product.count() > 0:
            return False, 'Product already exists'
        product = Product()
        product.product_title = form.product_title.data
        product.product_description = form.product_description.data
        product.product_category = form.product_category.data
        product.product_price = form.product_price.data
        isSaved, file_name = save_file(form.product_image.data, 'products')
        product.product_image = file_name
        try:
            db.session.add(product)
            db.session.commit()
            return True, 'Product added.'
        except Exception as e:
            return False, str(e)

    def get_products(self):
        products = Product.query.all()
        return products
    def get_product_categories(self):
        cats = Categories.query.filter_by(product_category=1).all()
        cats = [(str(c.cat_id), str(c.cat_title)) for c in cats]
        return cats


    def delete_product(self, id):
        product = Product.query.filter_by(product_id=id)
        if not product.count() > 0:
            return False, 'No such product found', 'error'

        product = product.first()
        delete_image(product.product_image, 'products')
        try:
            db.session.delete(product)
            db.session.commit()
            return True, 'Product deleted', 'success'
        except Exception as e:
            return False, str(e), 'error'