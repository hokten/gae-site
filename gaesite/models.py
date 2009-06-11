# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db
from django.contrib.auth.models import User

class Greeting(db.Model):
    author = db.ReferenceProperty(User)
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
