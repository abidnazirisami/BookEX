from mail.models import *
from pages.models import *
from request.models import *
from django.http import HttpResponseRedirect
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from django.shortcuts import redirect
from django.contrib.auth.models import User
from typing import List, Any
from web_project.forms import UploadFileForm
from web_project.urls import *


def messageCount(request):
	unread_messages = 0
	if request.user.is_authenticated:
		current_user = OurUser.objects.get(user = request.user)
		unread_messages = Message.objects.filter(to_user = current_user, seen = False).values('from_user').distinct().count()   

	return {
		'unread_messages': unread_messages,
	}

def pendingCount(request):
	count=0
	if request.user.is_authenticated:
		cur_user = OurUser.objects.get(user=request.user)
		to_receive = Boiii.objects.filter(receiver_id=cur_user, donated=True, received=False).exclude(id=cur_user).count()
		to_donate = Boiii.objects.filter(id=cur_user, donated=True, received=False).exclude(receiver_id=cur_user).count()
		want_to_donate = Boiii.objects.filter(id=cur_user, donated=False, received=False).exclude(receiver_id=cur_user).count()
		count = to_receive+to_donate+want_to_donate
	return {
		'pending_count': count,
	}

def notifications(request):
	form = UploadFileForm()
	notification_count=0
	will_donate_boiii = []
	will_donate_book = []
	will_donate_wish = []
	will_donate_count = []
	will_receive_boiii = []
	will_receive_book = []
	will_receive_wish = []
	will_receive_from = []
	if request.user.is_authenticated:
		current_user = request.user
		if not OurUser.objects.filter(user = current_user).exists():
			current_user.first_name = current_user.username
			current_user.save()
			current_profile = OurUser.objects.create(user = current_user, user_name = current_user.username)
		else:
			current_profile = OurUser.objects.get(user = current_user)

		##########################################################################################

		


		##########################################################################################
		

		# The books I have added to the library:
		can_donate_boiii = Boiii.objects.filter(id = current_profile, donated = False)
		
		for boi in can_donate_boiii:
			# The books that people except me have wished:
			lets_donate = Wishlist.objects.filter(isbn = boi.isbn.isbn).exclude(user = current_user) # Arrrgh
			print(lets_donate)
			for wish in lets_donate:
				# These are the books that I will be asked to donate in the notifications:
				will_donate_wish.append(wish)
				will_donate_book.append(Book.objects.get(isbn = wish.isbn))
				will_donate_boiii.append(Boiii.objects.filter(id = current_profile, isbn = wish.isbn, donated = False)[0])
				will_donate_count.append(len(Boiii.objects.filter(id = current_profile, isbn = wish.isbn, donated = False)))
				notification_count += 1
		# The wishes I made that has been met
		will_receive_boiii = Boiii.objects.filter(receiver_id = current_profile, donated = True, received = False)
		
		for boi in will_receive_boiii:
			print(boi.isbn)
			will_receive_book.append(boi.isbn) # For some reason, boi.isbn is a book type object -_-
			will_receive_wish.append(Wishlist.objects.get(isbn = boi.isbn.isbn, user = current_user))
			will_receive_from.append(User.objects.get(username = boi.id.user_name))
			notification_count += 1
	return {
		'notification_form':form, 
		'notification_donate':zip(will_donate_book,will_donate_boiii,will_donate_wish,will_donate_count), 
		'notification_receive':zip(will_receive_book,will_receive_boiii,will_receive_wish,will_receive_from), 
		'notification_count':notification_count,
	}
