import webapp2
from google.appengine.api.mail import EmailMessage

import jinja2
import os 





template_dir = os.path.join(os.path.dirname('__file__'),'templates')
env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)

class Handler(webapp2.RequestHandler):
    
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)
        
    def render_str(self,template,**params):
        t = env.get_template(template)
        return t.render(params)
    
    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))


class MainPage(Handler):
    
    
    def get(self):
        self.render('index.html')
        
class PhotoHandler(Handler):
    
    def get(self):
			
        self.render('photos.html')

        
class CareerHandler(Handler):
    def get(self):
        self.render('career.html')

    
class BlogHandler(Handler):
    
    def get(self):
		
		
        self.render('blog.html')
    
class ContactHandler(Handler):
    
    def get(self):
        self.render('contacts.html')

    def post(self):
        name = self.request.get('name')
        surname = self.request.get('surname')
        email = self.request.get('email')
        phone = self.request.get('phone')
        message = self.request.get('message')

        body = 'User %s,%s with email %s has sent you a message - %s' % (name,surname,email,message)

        my_mail = EmailMessage(sender='jkimuli@gmail.com',to='jkimuli@gmail.com',subject='Hi',body=body)

        #send email

        my_mail.check_initialized()
        my_mail.send()
    


app = webapp2.WSGIApplication([('/', MainPage),('/photos',PhotoHandler),('/contact',ContactHandler),('/career',CareerHandler),('/blog',BlogHandler)], debug=True)



