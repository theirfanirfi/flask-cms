from application.Models.models import *
class BF:
    @staticmethod
    def getBL(blName):
        pass

class MF:
    @staticmethod
    def getModel(modelName):
        if modelName == "post":
            return Post()
        elif modelName == "user":
            return User()
