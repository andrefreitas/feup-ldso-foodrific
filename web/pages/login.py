import webapp2
import cgi

class Login(webapp2.RequestHandler):
    
    def post(self):
        email = cgi.escape(self.request.get('email'))
        password = cgi.escape(self.request.get('password'))
        
        self.response.write(email)
        self.response.write(password)
