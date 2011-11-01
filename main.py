#!/usr/bin/python
# -*- coding: UTF-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp import template
from django.utils import simplejson as json


class MainHandler(webapp.RequestHandler):

    def post(self):

        _file = self.request.POST['arquivo'].file.read()
        data = json.loads(_file)

        i = 1
        for _o in data["friends"]:
            link = _o["profileIds"][0]
            self.response.out.write('%i - <a href="https://plus.google.com/u/0/%s" target="_black">https://plus.google.com/u/0/%s</a> <br />' % (i, link, link))
            i = i +1

    def get(self):

        self.redirect('/')


class Upload(webapp.RequestHandler):

    def get(self):
        self.response.out.write(
                template.render('template/index.html',{}))


def main():
    application = webapp.WSGIApplication([
        ('/', Upload),
        ('/send', MainHandler),
        ],debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
