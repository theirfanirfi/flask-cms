from application import db
from application.Models.models import Partner
from application.utils import save_file, delete_image
class PartnerBL:
    def add_partner(self, form):
        partner = Partner.query.filter_by(partner_title=form.partner_title.data)
        if partner.count() > 0:
            return False, 'Partner already exists'
        partner = Partner()
        partner.partner_title = form.partner_title.data
        isSaved, file_name = save_file(form.partner_image.data, 'partners')
        partner.partner_image = file_name
        try:
            db.session.add(partner)
            db.session.commit()
            return True, 'Partner added.'
        except Exception as e:
            return False, str(e)

    def get_partners(self):
        partners = Partner.query.all()
        return partners



    def delete_partner(self, id):
        partner = Partner.query.filter_by(partner_id=id)
        if not partner.count() > 0:
            return False, 'No such partner found', 'error'

        partner = partner.first()
        delete_image(partner.partner_image,'partners')
        try:
            db.session.delete(partner)
            db.session.commit()
            return True, 'partner deleted', 'success'
        except Exception as e:
            return False, str(e), 'error'