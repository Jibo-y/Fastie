from google.appengine.ext import ndb

class Emetrocard(ndb.Model):
    Emetrocard_line1 = ndb.StringProperty(required=True)
    Emetrocard_line2 = ndb.StringProperty(required=True)
    Emetrocard_choice = ndb.StringProperty(required=True)
    Emetrocard_balance = ndb.FloatProperty(required= True)
    url= ndb.StringProperty(required=True, default="https://upload.wikimedia.org/wikipedia/en/8/8b/MetroCard.SVG")
