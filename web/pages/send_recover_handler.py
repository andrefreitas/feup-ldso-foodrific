import webapp2
import cgi
from base_handler import *
from datastore import *

class SendRecoverHandler(BaseHandler):

    def post(self):
    	email = self.request.get("emailToRecover")
        try:
            if(isUser(email)):
                generateUserRecoveryToken(email)
                return self.redirect('/?message=Email enviado com sucesso!')
            else:
                return self.redirect('/login?message=Email invalido!')
        except:
            return self.redirect('/login?message=Email invalido!')