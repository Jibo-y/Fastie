import webapp2
import jinja2
import os
import random
from models import Emetrocard

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_Emetrocard():
    Emetrocard_type=["show your current balance"]
    return(random.choice(Emetrocard_type))

class ShowbalanceHandler(object):
    def __init__(self, balance):
        self.balance = balance

        self.response.write('this is your current balance in the card')

    def __str__(self):
        return("the balance in the account %s USD" %( self.balance))

    def deposit(self, d_amount):
        if d_amount < 0:
            print("add balance into your card")
        else:
            self.balance = self.balance + d_amount

class EmetrocardHandler(webapp2.requestHandler):
    def get(self):
        Emetrocard_template = the_jinja_env.get_template('templates/E-metrocard.html')

        self.response.write(e-metrocard_template.render())

    def post(self):
        Emetrocard_card_number = self.request.get('user-card-number')
        Emetrocard_card_expiration_date = self.request.get('user-expiration-date')
        Emetrocard_img_choice = self.request.get('Emetrocard-type')

        user_Emetrocard = Emetrocatd(
            Emetrocard_line1 = Emetrocard_first_line,
            Emetrocard_line2 = Emetrocard_second_line,
            pic_type = Emetrocard_img_choice

        )

        user_Emetrocard.put()

class serviceHandler(webapp2.requestHandler):
    def get(self):
        service_template = the_jinja_env.get_template('templates/trainservices.html')

app = webapp2.WSGIApplication([
    ('/', EmetrocardHandler),
    ('/Emetrocard', ShowbalanceHandler),
    ('/service', serviceHandler)
], debug=True)
