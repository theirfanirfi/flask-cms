from application import db
from application.Models.models import Pages


class PageBL:
    def add_page(self, form):
        pages = Pages.query.filter_by(page_title=form.page_title.data)
        if pages.count() > 0:
            return False, 'Pages already exists'
        pages = Pages()
        pages.page_title = form.page_title.data
        pages.page_description = form.page_description.data
        try:
            db.session.add(pages)
            db.session.commit()
            return True, 'Page added.'
        except Exception as e:
            return False, str(e)

    def update_page(self, form, id):
        page = Pages.query.filter_by(page_id=id)
        if not page.count() > 0:
            return False, 'Page not found.'
        page = page.first()
        page.page_title = form.page_title.data
        page.page_description = form.page_description.data
        try:
            db.session.add(page)
            db.session.commit()
            return True, 'Page updated.'
        except Exception as e:
            return False, str(e)

    def get_pages(self):
        pages = Pages.query.all()
        return pages
    def get_page_by_id(self, id):
        page = Pages.query.filter_by(page_id=id)
        if not page.count() > 0:
            return False, 'Page not found', 'error'
        page = page.first()
        return True, page, 'success'

    def delete_page(self, id):
        pages = Pages.query.filter_by(page_id=id)
        if not pages.count() > 0:
            return False, 'No such Page found', 'error'

        pages = pages.first()
        try:
            db.session.delete(pages)
            db.session.commit()
            return True, 'Page deleted', 'success'
        except Exception as e:
            return False, str(e), 'error'

    def get_contact_page_for_frontend_link(self):
        search_term = "%{}%".format("contact")
        page = Pages.query.filter(Pages.page_title.like(search_term))
        if page.count() > 0:
            return page.first()
        return False