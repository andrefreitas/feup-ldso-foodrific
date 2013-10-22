import webapp2
import cgi
import datetime

class Register(webapp2.RequestHandler):
    
    def post(self):
        # Obter dados do formulario
        name = cgi.escape(self.request.get('name'))
        email = cgi.escape(self.request.get('email'))
        password = cgi.escape(self.request.get('password'))
        gender = cgi.escape(self.request.get('gender'))
        day_birthday = cgi.escape(self.request.get('day'))
        month_birthday = cgi.escape(self.request.get('month'))
        year_birthday = cgi.escape(self.request.get('year'))
        
        # Construir uma data valida para ser inserida na base de dados
        birthday_date = datetime.date(int(year_birthday), int(month_birthday), int(day_birthday))
        
        self.response.write(name);
        self.response.write(email);
        self.response.write(password);
        self.response.write(gender);
        self.response.write(birthday_date);
        
        