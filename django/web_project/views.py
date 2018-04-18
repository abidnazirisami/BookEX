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
			donated_list = Boiii.objects.filter(id_id = userid)
		#print(donated_list)
		requested_list = []
		user_list = []
		profile_list=[]
		for donate_worthy in donated_list:
			cur_isbn = donate_worthy.isbn.isbn
			#print(cur_isbn)
			if Wishlist.objects.filter(isbn = cur_isbn):
				wished_object = list(Wishlist.objects.filter(isbn = cur_isbn))
				#print(wished_object)
				for wish in wished_object:
					requested_list.append(wish)
					cur_user = list(OurUser.objects.filter(user_id = wish.user_id))
					user_list.append(cur_user[0])
					profile_list.append(User.objects.get(username=cur_user[0].user_name))
					#print(cur_user[0])
					#print(wish)
		#print(requested_list)
		print(profile_list)
		return render(request,'home.html',context={'request_list':zip(requested_list,user_list, profile_list)})
	return render(request, 'home.html')

def about(request):
	return render(request,'about.html')


def contact(request):
	return render(request,'contact.html')