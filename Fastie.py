import webapp2
import jinja2
import os
from models import Fastie

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class WelcomeHandler(webapp2.requestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')

 class ShowAboutHandler(webapp2.requestHandler):
     def get(self):
         about_template = the_jinja_env.get_template('templates/welcome.html')
