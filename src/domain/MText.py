class MText(object):

    def __init__(self, payload):
        self.payload = payload

    def __str__(self):
        return "%s" % self.payload
