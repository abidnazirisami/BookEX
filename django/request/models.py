# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Wishlist(models.Model):
	id = models.AutoField(max_length=50,primary_key=True)
	user = models.ForeignKey(User, related_name='request_user',on_delete=models.DO_NOTHING,default='Not available')
	isbn = models.CharField(max_length=50, default='Not available')	
	author_name = models.CharField(max_length=500,default='Not available')
	edition = models.IntegerField(default = 1)
	count = models.IntegerField(default = 1)
	book_name = models.CharField(max_length=100,default='Not available')
	isAvailable = models.BooleanField(default=False)
	hasReceived = models.BooleanField(default=False)
	isEmergency = models.BooleanField(default=False)
	request_date = models.DateField(auto_now=False, auto_now_add=True)
