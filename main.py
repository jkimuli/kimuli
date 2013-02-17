import webapp2

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
    
class ProjectHandler(Handler):
    
    def get(self):
        self.render('projects.html')
    
class ContactHandler(Handler):
    
    def get(self):
        self.render('contacts.html')
    


app = webapp2.WSGIApplication([('/', MainPage),('/photos',PhotoHandler),('/contact',ContactHandler),('/career',CareerHandler),('/projects',ProjectHandler)], debug=True)



