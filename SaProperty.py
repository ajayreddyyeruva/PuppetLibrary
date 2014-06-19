import ConfigParser


class SaProperty(object):
    
    def __init__(self, propertyFilePath):
        self.config = ConfigParser.ConfigParser()
        self.propertyFilePath = propertyFilePath
        self.propertiesList=[]
        self._parsePropertyFile()
        
    def _parsePropertyFile(self):
        self.config.read(self.propertyFilePath)
        self.propertiesList = self.config.items("DEFAULT")
        self.propertiesDict=dict((self.property[0], self.property[1]) for self.property in self.propertiesList)
        
    def getKeys(self):
        return self.propertiesDict.keys()

if __name__ == "__main__":
    saProperty1=SaProperty('/home/sandy/tmp.test.property')
    print saProperty1.getKeys()
