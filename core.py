import requests
import urllib3
import glob, os
from pathlib import Path

EXT_DIR = 'extentions'
WEB_JOB_QUEUE = {}
DEBUG = False

def register_module(ext_module):
    if ext_module.__category__ == 'web':
        if DEBUG: print('+ %s - Registrated as %s' % (ext_module.__doc__, ext_module.__category__))
        global WEB_JOB_QUEUE
        WEB_JOB_QUEUE[ext_module] = []
        return True

def loads_modules():
    pwd = os.path.join(os.getcwd(), EXT_DIR)
    for module in glob.glob(pwd + "/*.py"):
        try:
           if DEBUG: print('+ Load module: %s' % module)
           load_str_module = "{}.{}".format(EXT_DIR, Path(module).name.split('.')[0])
           ext_module =  __import__ (load_str_module, fromlist=[None])
           if not register_module(ext_module):
               raise Exception("- Cannot register module: %s" % (module))
        except Exception as e:
             if DEBUG: print('- Error loading module: %s (%s)' % (module, str(e)))

def RunAllWebScans(url = ''):
    for ext in WEB_JOB_QUEUE:
            mod = ext.Extention(url=url)
            try:
                result = mod.run()
                if result:
                    WEB_JOB_QUEUE[ext] = result
            except Exception as e:
                print('- Extention %s error: %s' % (ext, e))
    
    if DEBUG: print('+ Web done')


def CallWebRequest(host, url='', payload=''):

    #import requests

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    HTTP_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    s = requests.Session()
    # s.proxies = proxy
    s.verify = False
    req = requests.Request(method='GET', url=host)
    prep = req.prepare()
    prep.headers = HTTP_HEADERS
    prep.url = host + (url or payload)
    prep.allow_redirects = False
    try:
        r = s.send(prep, allow_redirects=False)
        return r
    except Exception as e:
       # if __DEBUG__:
            #print('Module {} has exception: {}'.format(__module__, str(e)))
        return False