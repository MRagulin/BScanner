from selenium import webdriver
from datetime import datetime
from os import getcwd, path

__doc__ = "Web page screenshot loader"
__category__ = "web"

class Extention():
    def __init__(self, url='', out=""):
        if url == '':
             raise Exception('URL for screenshot empty')
             return False
        
        self.driver = webdriver.Chrome()
        self.url = url
        
        if out == '':
             random_name = datetime.now()
             random_name = int(random_name.strftime('%Y%m%d%H%M%S'))
             out = "{}.{}.png".format(self.url.split('//')[1].replace('/', ''), random_name)  
             out = path.join(getcwd(), 'logs', out)
        self.out = out

    def run(self):
        self.driver.get(self.url)
        if self.driver.save_screenshot(self.out):
            print('+ Screeshot save in %s' % (self.out))
        else:
            raise Exception('Screeshot not save')
        self.driver.quit()
        return self.out
