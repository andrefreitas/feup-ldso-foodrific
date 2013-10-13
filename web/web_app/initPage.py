import cgi
import webapp2

INIT_PAGE = """\
<!DOCTYPE html>
<html>
  <body>
    <form action="" method="post">
		First name: <input type="text" name="firstname">
		<br>
		Last name: <input type="text" name="lastname">
    </form>
  </body>
</html>
"""

class InitPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(INIT_PAGE)