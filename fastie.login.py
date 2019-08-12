from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      self.response.write("You're logged in!")
    else:
        login_url = users.create_login_url('/')
      self.response.write("You're not logged in please try again" + login_html)
