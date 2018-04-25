from django.db import models
from pages.models import *
# Create your models here.
class Message(models.Model):
	to_user = models.ForeignKey(OurUser,on_delete = models.CASCADE,related_name='receiver')
	from_user = models.ForeignKey(OurUser,on_delete = models.CASCADE,related_name='sender')
	text = models.CharField(max_length=256,default='')
	sent_on = models.DateTimeField(auto_now_add=True)
	seen = models.BooleanField(default = False)
	photo = models.ImageField(blank = True)
