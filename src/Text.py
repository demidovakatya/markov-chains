class Text(object):
    def __init__(self, payload, url = ''):
        self.payload = payload
        self.url = url

    def __repr__(self):
        return "(%s): %s" % (self.url, self.payload)
