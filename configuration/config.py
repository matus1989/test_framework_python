import configparser, os

class Configuration:
    
    
    def __init__(self,conf="DEFAULT") -> None:
        self.config = configparser.ConfigParser()
        ini_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        self.config.read(ini_file_path)
        self.settings = self.config[conf]
        
        self.url = self.get("URL")
        
    def get(self, key, fallback=None):
        return self.settings.get(key) 
 
 
 
 
if __name__ == "__main__":
     conf = Configuration("DEFAULT")
     print(conf.URL)