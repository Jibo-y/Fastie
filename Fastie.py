import webapp2
import jinja2
import os
from model import Emetrocard
from google.appengine.api import users

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class welcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/index.html')
        variable_dict = {
        "login_url": users.create_login_url('/'),
        "logout_url":users.create_logout_url('/'),
        }
        self.response.write(welcome_template.render(variable_dict))

class EmetrocardHandler(webapp2.RequestHandler):
    def get(self):
        Emetrocard_template = the_jinja_env.get_template('templates/E-metrocard.html')

        self.response.write(Emetrocard_template.render())

    def post(self):
        Emetrocard_card_number = self.request.get('user-card-number')
        Emetrocard_card_expiration_date = self.request.get('user-expiration-date')
        Emetrocard_choice = self.request.get('Emetrocard-type')

        user_Emetrocard = Emetrocard(
            Emetrocard_line1 = Emetrocard_card_number,
            Emetrocard_line2 = Emetrocard_expiration_date,
            Emetrocard_choice = Emetrocard_choice,
            Emetrocard_balance = random.choice()
        )
        user_Emetrocard.put()

    def deposit(self, d_amount):
        if d_amount < 0:
            print("add balance into your card")
        else:
            self.Emetrocard_balance = self.Emetrocard_balance + d_amount
            user_Emetrocard.put()

class serviceHandler(webapp2.RequestHandler):
    def get(self):
        service_template = the_jinja_env.get_template('templates/trainservices.html')
        self.response.write(Emetrocard_template.render())

class ScheduleHandler(webapp2.RequestHandler):
    def get(self):
        schedule_template = the_jinja_env.get_template('templates/schedule.html')
        self.response.write(Emetrocard_template.render())

app = webapp2.WSGIApplication([
    ('/', welcomeHandler),
    ('/Emetrocard', EmetrocardHandler),
    ('/service', serviceHandler),
    ('/schedule', ScheduleHandler)
], debug=True)
