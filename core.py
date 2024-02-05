import glob, os
import importlib
from pathlib import Path

EXT_DIR = 'extentions'
WEB_JOB_QUEUE = {}

def register_module(ext_module):
    if ext_module.__category__ == 'web':
        print('+ %s - Registrated as %s' % (ext_module.__doc__, ext_module.__category__))
        global WEB_JOB_QUEUE
        WEB_JOB_QUEUE[ext_module] = []
        return True

def loads_modules():
    pwd = os.path.join(os.getcwd(), EXT_DIR)
    for module in glob.glob(pwd + "/*.py"):
        try:
           print('+ Load module: %s' % module)
           load_str_module = "{}.{}".format(EXT_DIR, Path(module).name.split('.')[0])
           ext_module =  __import__ (load_str_module, fromlist=[None])
           if not register_module(ext_module):
               raise Exception("- Cannot register module: %s" % (module))
        except Exception as e:
            print('- Error loading module: %s (%s)' % (module, str(e)))


if __name__ == "__main__":
    loads_modules()
    test = 'https://localhost:8080/'

    for ext in WEB_JOB_QUEUE:
        mod = ext.Extention(url=test)
        try:
            result = mod.run()
            if result:
                WEB_JOB_QUEUE[ext] = result
        except Exception as e:
            print('- Extention %s error: %s' % (ext, e))
    print(WEB_JOB_QUEUE)
    print('Done')