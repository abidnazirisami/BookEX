from django.shortcuts import *
from django.urls import *
from pages.models import *
from request.models import *
from .models import *
from django.http import HttpResponseRedirect
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from django.shortcuts import redirect
from django.contrib.auth.models import User
from typing import List, Any

def rate(request, isbn):
	if request.method=="POST":
		current_user = request.user
		print(request.POST['rating'])
		print(request.POST['review'])
		cur_review = request.POST['review']
		cur_rating = request.POST['rating']
		cur_user = OurUser.objects.get(user = current_user)
		cur_book = Book.objects.get(isbn = isbn)
		cur_to_save = Review(user_id = cur_user, isbn = cur_book, review = cur_review, rating = cur_rating)
		cur_count = Review.objects.filter(isbn = cur_book).count()
		total_rating = 0.0
		total_rating = (cur_count*cur_book.rating  + float(cur_rating))/(cur_count+1)
		cur_book.rating = total_rating
		cur_book.save()
		cur_to_save.save()
		return redirect('viewbookprofile', req_isbn=isbn)	
	else:
		print(isbn)
		print(request.user.username)
		return render(request, 'rating/ratings.html')