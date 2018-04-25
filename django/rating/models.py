from django.db import models
from pages.models import *

# Create your models here.
class Review(models.Model):
	user_id = models.ForeignKey(OurUser, related_name="userid", on_delete=models.CASCADE)
	review = models.CharField(max_length=10000,default=False)
	rating = models.FloatField(default = 5.0)
	isbn = models.ForeignKey(Book, on_delete=models.CASCADE,default='Not available')
	rate_date = models.DateField(auto_now=True)