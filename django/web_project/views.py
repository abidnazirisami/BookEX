from django.shortcuts import render
from django.urls import *
from pages.models import *
from request.models import *
from django.http import HttpResponseRedirect
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from django.shortcuts import redirect
from django.contrib.auth.models import User
from typing import List, Any


def homepage(request):
	current_user = request.user
	if current_user.is_authenticated:
		if not OurUser.objects.filter(user=current_user).exists():
			current_user.first_name = current_user.username
			current_user.save()
			newUser = OurUser.objects.create(user = current_user,user_name = current_user.username)
		userid = OurUser.objects.get(user = current_user)
		donated_list =[]
		if Boiii.objects.filter(id_id = userid).exists():
			donated_list = Boiii.objects.values('id_id','isbn_id').filter(id_id = userid).distinct()
		print(donated_list)
		requested_list = []
		user_list = []
		profile_list=[]
		notification_count=0
		book_count = []
		for donate_worthy in donated_list:
			cur_isbn = donate_worthy['isbn_id']
			#print(cur_isbn)
			if Wishlist.objects.filter(isbn = cur_isbn):
				wished_object = list(Wishlist.objects.filter(isbn = cur_isbn))
				#print(wished_object)
				for wish in wished_object:
					requested_list.append(wish)
					book_count.append( Boiii.objects.values('id_id','isbn_id').filter(id_id = userid,isbn_id = cur_isbn).count())
					cur_user = list(OurUser.objects.filter(user_id = wish.user_id))
					user_list.append(cur_user[0])
					profile_list.append(User.objects.get(username=cur_user[0].user_name))
					notification_count+=1
					#print(cur_user[0])
					#print(wish)
		#print(requested_list)
		#print(profile_list)
		if request.method=="POST":
			################################################################
			# For Raida:
			print(request.POST['username'])
			print(request.POST['isbn'])
			################################################################
		return render(request,'home.html',context={'request_list':zip(requested_list,user_list, profile_list,book_count),'notification_count':notification_count})
	return render(request, 'home.html')

def about(request):
	return render(request,'about.html')


def contact(request):
	return render(request,'contact.html')
