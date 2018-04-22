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
from .forms import UploadFileForm


def sideNav(request, current_user):
	if not OurUser.objects.filter(user=current_user).exists():
		current_user.first_name = current_user.username
		current_user.save()
		newUser = OurUser.objects.create(user = current_user,user_name = current_user.username)
	userid = OurUser.objects.get(user = current_user)
	if request.method=="POST":
		################################################################
		# For Raida:
		form = UploadFileForm(request.POST, request.FILES)
		#print(request.FILES)
		#print(request.POST['username'])
		#print(request.POST['isbn'])
		#print(request.POST['condition'])
		donate_isbn = request.POST['isbn']
		donate_condition = request.POST['condition']
		receiver = request.POST['username']
		donor = userid
		donate_book = Boiii.objects.filter(isbn=donate_isbn, id=donor, donated=False)[0]
		donate_book.donated = True
		if form.is_valid(): 
			if 'Photo' in request.FILES:
				donate_book.photo = request.FILES['Photo']
		donate_book.condition=donate_condition
		donate_book.receiver_id=OurUser.objects.get(user_name=request.POST['username']) 
		donate_book.save()
		################################################################
	form = UploadFileForm()
	donated_list =[]
	if Boiii.objects.filter(id_id = userid).exists():
		donated_list = Boiii.objects.values('id_id','isbn_id').filter(id_id = userid).distinct()
	print(donated_list)
	requested_list = []
	user_list = []
	profile_list=[]
	notification_count=0
	book_count = []
	wished_list = []
	wished_user_list = []
	wished_profile_list = []
	wished_book_count = []
	for donate_worthy in donated_list:
		cur_isbn = donate_worthy['isbn_id']
		#print(cur_isbn)
		if Wishlist.objects.filter(isbn = cur_isbn):
			wished_object = list(Wishlist.objects.filter(isbn = cur_isbn).exclude())
			#print(wished_object)
			for wish in wished_object:
				cur_count = Boiii.objects.values('id_id','isbn_id').filter(id_id = userid,isbn_id = cur_isbn, donated=False).count()
				if cur_count > 0:
					requested_list.append(wish)
					book_count.append(cur_count)
					cur_boiii = Boiii.objects.filter(id_id = userid,isbn_id = cur_isbn, donated=False)
					cur_boiii_ob = cur_boiii[0]
					cur_user = list(OurUser.objects.filter(user_id = cur_boiii_ob.id_id))
					user_list.append(cur_user[0])
					profile_list.append(User.objects.get(username=cur_user[0].user_name))
					notification_count+=1
					
				cur_wish_count = Boiii.objects.values('id_id', 'isbn_id').filter(receiver_id_id=userid, isbn_id=cur_isbn, donated=True, received = False).exclude(id_id=userid).count()
				if cur_wish_count > 0:
					wished_list.append(wish)
					wished_book_count.append(cur_count)
					cur_boiii = Boiii.objects.filter(receiver_id_id=userid, isbn_id=cur_isbn, donated=True, received = False).exclude(id_id=userid)
					cur_boiii_ob = cur_boiii[0]
					cur_user = list(OurUser.objects.filter(user_id=cur_boiii_ob.id_id))
					wished_user_list.append(cur_user[0])
					wished_profile_list.append(User.objects.get(username=cur_user[0].user_name))
					notification_count += 1
	return form,requested_list,user_list,profile_list,book_count,notification_count,wished_list,wished_user_list,wished_profile_list,wished_book_count
def homepage(request):
	current_user = request.user
	if current_user.is_authenticated:
		form,requested_list,user_list,profile_list,book_count,notification_count,wished_list,wished_user_list,wished_profile_list,wished_book_count=sideNav(request, current_user)
		return render(request,'home.html',context={'form':form,'request_list':zip(requested_list,user_list, profile_list,book_count),'notification_count':notification_count,'wished_list': zip(wished_list,wished_user_list, wished_profile_list,wished_book_count),})
	return render(request, 'home.html')

def about(request):
	return render(request,'about.html')


def contact(request):
	return render(request,'contact.html')
