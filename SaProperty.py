import ConfigParser


class SaProperty(object):
    
    config = ConfigParser.ConfigParser()
    
    def __init__(self, propertyFilePath):
        self.propertyFilePath = propertyFilePath
        self.config.read(propertyFilePath)
        self._parsePropertyFile()
        
    def _parsePropertyFile(self):
        self.config.read(self.propertyFilePath)
        self.propertiesList = self.config.items("DEFAULT")
        #print self.propertiesList
        self.propertiesDict=dict((self.property[0], self.property[1]) for self.property in self.propertiesList)
        #print self.propertiesDict
        
    def _getKeys(self):
        return self.propertiesDict.keys()
        
            
if __name__ == "__main__":
    saProperty=SaProperty('/home/sandy/test.property')
    print saProperty._getKeys()
