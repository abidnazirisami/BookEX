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

@login_required
def rate(request, isbn):
	if request.method=="POST":
		current_user = request.user
		print(request.POST['rating'])
		print(request.POST['review'])
		cur_review = request.POST['review']
		cur_rating = request.POST['rating']
		cur_user = OurUser.objects.get(user = current_user)
		cur_book = Book.objects.get(isbn = isbn)
		# If this user has reviewed the book before
		if Review.objects.filter(user_id = cur_user, isbn = cur_book).exists():
			cur_to_save = Review.objects.get(user_id = cur_user, isbn=cur_book)
			cur_count = Review.objects.filter(isbn = cur_book).count()
			total_rating = 0.0
			total_rating = (cur_count*cur_book.rating  + float(cur_rating) - cur_to_save.rating)/(cur_count)
			cur_book.rating = total_rating
			cur_to_save.rating = float(cur_rating)
			if len(cur_review)>0:
				cur_to_save.review = cur_review
		else:			
			cur_to_save = Review(user_id = cur_user, isbn = cur_book, review = cur_review, rating = cur_rating)
			cur_count = Review.objects.filter(isbn = cur_book).count()
			total_rating = 0.0
			total_rating = (cur_count*cur_book.rating  + float(cur_rating))/(cur_count+1)
			cur_book.rating = total_rating
		cur_book.save()
		cur_to_save.save()
		return redirect('viewbookprofile', req_isbn=isbn)	
	else:
		cur_user = OurUser.objects.get(user = request.user)
		cur_book = Book.objects.get(isbn = isbn)
		placeholder = 'Write your review here . . .'
		if Review.objects.filter(user_id = cur_user, isbn = cur_book).exists():
			placeholder='Previously you wrote: '
			placeholder+=Review.objects.get(user_id = cur_user, isbn=cur_book).review
			placeholder+=' (Leave blank to keep unchanged)'
		print(isbn)
		print(request.user.username)
		return render(request, 'rating/ratings.html', context={'placeholder':placeholder})