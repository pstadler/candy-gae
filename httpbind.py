import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
from google.appengine.runtime import apiproxy_errors

DEBUG = True
DESTINATION = 'http://yourhost.com:5280/http-bind/'

class HTTPBind(webapp.RequestHandler):
	def get(self):
		self.response.out.write(self.proxy());
		
	def post(self):
		self.response.out.write(self.proxy(True));
		
	def proxy(self, post=False):
		try:
			if(post):
				response = urlfetch.fetch(DESTINATION, self.request.body, 'POST', {}, False, True, 10)
			else:
				response = urlfetch.fetch(DESTINATION, None, 'GET', {}, False, True, 10)
		except (urlfetch.Error, apiproxy_errors.Error):
			logging.exception("Could not fetch URL")
			return None
		
		return response.content

application = webapp.WSGIApplication([('/http-bind/', HTTPBind)], debug=DEBUG)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()

