from application import db
from application.Models.models import SMLink
class SMLinksBL:
	def addOrUpdateLinks(self, form):
		link = SMLink.query.filter(SMLink.fb_link!='')
		if link.count() > 0:
			link = link.first()
		else:
			link = SMLink()
		link.fb_link = form.fb_link.data
		link.twitter_link = form.twitter_link.data
		link.instagram_link = form.instagram_link.data
		link.google_plus_link = form.google_plus_link.data
		link.linkedin_link = form.linkedin_link.data
		try:
			db.session.add(link)
			db.session.commit()
			return True, 'Links updated.'
		except Exception as e:
			return False, str(e)

	def get_links(self):
		links =  SMLink.query.filter(SMLink.fb_link != '')
		if links.count() > 0:
			return True, links.first()
		else:
			return False, 'Links not found'

	def get_links_for_frontend(self):
		links =  SMLink.query.filter(SMLink.fb_link != '')
		if links.count() > 0:
			return links.first()
		else:
			return False