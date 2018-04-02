# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Author(models.Model):
	author_id = models.CharField(max_length=50,primary_key=True,default='Not available')
	author_name = models.CharField(max_length=100,default='Not available')
	wiki_link = models.CharField(max_length=500,default='Not available')
	rating = models.FloatField(default=0.0)

class Book(models.Model):
	isbn = models.CharField(max_length=50, primary_key=True,default='Not available')	
	author_id = models.ForeignKey(Author, on_delete=models.CASCADE,default='Not available')
	topic_name = models.CharField(max_length=100,default='Not available')
	publish_date = models.DateField(default = "17-02-1996")
	publisher = models.CharField(max_length=100,default='Not available')
	amazon_link = models.CharField(max_length=500,default='Not available')
	edition = models.IntegerField(default = 1)
	pages = models.IntegerField(default = 1)
	count = models.IntegerField(default = 0)
	rating = models.FloatField(default = 0.0)
	book_name = models.CharField(max_length=100,default='Not available')

class OurUser(models.Model):
	user = models.OneToOneField(User, related_name='user',on_delete=models.DO_NOTHING,)    
	user_name = models.CharField(max_length=100,default='Not available')
	batch = models.IntegerField(default = 21)
	roll = models.IntegerField(default = 26)
	mail_id = models.CharField(max_length=100,default='Not available')
	donate_count = models.IntegerField(default = 0)
	phone = models.CharField(max_length=100,default='Not available')

class Boiii(models.Model):
	book_id = models.CharField(max_length=50, primary_key=True,default='Not available')	
	isbn = models.ForeignKey(Book, on_delete=models.CASCADE,default='Not available')
	id = models.ForeignKey(OurUser, on_delete=models.CASCADE)
	condition = models.FloatField(default = 0.0)
