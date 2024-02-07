__doc__ = "Check security headers"
__category__ = "web"
__severity__ = "info"
__header__ = "Check security headers"
__info__ = "Check security headers"

from core import CallWebRequest
import json

rules = {'strict-transport-security': {'value':['max_age']}, 
        'x-xss-protection': {'value':['1']}, 
        'x-frame-options': {'value': ['deny', 'sameorigin']},
        'content-security-policy' : {'value': []},
        'access-control-allow-origin': {'value': []},
        }
class Extention():
    def __init__(self, url=''):
        if url == '':
             raise Exception('- Plugin error ("%s") URL empty' % (__doc__))
        self.url = url

    def run(self):
        results = CallWebRequest(host=self.url)
        result = '{}\n{}'.format(results.headers, results.text)
        if len(results.headers) > 0:
            header = json.dumps(dict(results.headers))
            for rule in rules:
                if rule not in header.lower():
                    print('- Security header {} not set'.format(rule))
        return result
