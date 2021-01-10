from application import db
from application.Models.models import Settings
class SettingsBL:
	def addOrUpdateSetting(self, form):
		setting = Settings.query.filter_by(setting_type='footer')
		if setting.count() > 0:
			setting = setting.first()
		else:
			setting = Settings()
		setting.setting_type = 'footer'
		setting.setting_description = form.setting_description.data
		try:
			db.session.add(setting)
			db.session.commit()
			return True, 'Footer updated.'
		except Exception as e:
			return False, str(e)

	def get_footerSettingObject(self):
		setting = Settings.query.filter_by(setting_type='footer')
		if setting.count() > 0:
			return True, setting.first()
		else:
			return False, 'Links not found'

	def get_footer_setting_frontend(self):
		setting = Settings.query.filter_by(setting_type='footer')
		if setting.count() > 0:
			return setting.first()
		else:
			return False