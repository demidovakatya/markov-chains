class Text(object):

    def __init__(self, source, payload, url=''):
        self.source = source
        self.payload = payload
        self.url = url

    def __str__(self):
        return "Source: %s, URL: %s, Payload: %s" % (self.source, self.url, self.payload)
