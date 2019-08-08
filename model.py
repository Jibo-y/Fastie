from google.appengine.ext import ndb

class Emetrocard(ndb.Model):
    Emetrocard_line1 = ndb.StringProperty(required=True)
    Emetrocard_line2 = ndb.StringProperty(required=True)
    Emetrocard_type = ndb.StringProperty(required=True)
