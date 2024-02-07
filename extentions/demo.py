__doc__ = "Test module"
__category__ = "web"
__severity__ = "info"
__header__ = "Test module"
__info__ = "Test description"

class Extention():
    def __init__(self, url=''):
        if url == '':
             raise Exception('- Plugin error ("%s") URL empty' % (__doc__))
        self.url = url

    def run(self):
        result = '+ %s test - ok' % (__doc__)
        return result
