import webapp2
import jinja2
import os
import foodrific.sign
import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class InitialPage(webapp2.RequestHandler):

    def get(self):
        
        # Obter data para usar para a data de nascimento
        now = datetime.datetime.now()
        total_day = 32
        total_month = 13
        total_year = now.year + 1
        
        template_values = {
                           'total_day': total_day,
                           'total_month': total_month,
                           'total_year': total_year,}
        
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', InitialPage),
    ('/sign', foodrific.sign.LoginPage)
], debug=True)



