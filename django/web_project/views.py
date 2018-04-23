from django.shortcuts import *
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
from .urls import *

@login_required
def notifications(request):
	current_user = request.user
	if not OurUser.objects.filter(user = current_user).exists():
		current_user.first_name = current_user.username
		current_user.save()
		current_profile = OurUser.objects.create(user = current_user, user_name = current_user.username)
	else:
		current_profile = OurUser.objects.get(user = current_user)

	##########################################################################################

	form = UploadFileForm()


	##########################################################################################
	notification_count=0

	# The books I have added to the library:
	can_donate_boiii = Boiii.objects.filter(id = current_profile, donated = False)
	will_donate_boiii = []
	will_donate_book = []
	will_donate_wish = []
	will_donate_count = []
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
	will_receive_book = []
	will_receive_wish = []
	will_receive_from = []
	for boi in will_receive_boiii:
		print(boi.isbn)
		will_receive_book.append(boi.isbn) # For some reason, boi.isbn is a book type object -_-
		will_receive_wish.append(Wishlist.objects.get(isbn = boi.isbn.isbn, user = current_user))
		will_receive_from.append(User.objects.get(username = boi.id.user_name))
		notification_count += 1
	return form, zip(will_donate_book,will_donate_boiii,will_donate_wish,will_donate_count), zip(will_receive_book,will_receive_boiii,will_receive_wish,will_receive_from), notification_count


def homepage(request):
	current_user = request.user
	
	if current_user.is_authenticated:
		if not OurUser.objects.filter(user = current_user).exists():
			current_user.first_name = current_user.username
			current_user.save()
			current_profile = OurUser.objects.create(user = current_user, user_name = current_user.username)
		else:
			current_profile = OurUser.objects.get(user = current_user)
		form, donate, receive, notification_count = notifications(request)
		return render(request,'home.html',context={'form':form,'donate':donate,'receive': receive, 'notification_count' : notification_count})
	return render(request, 'home.html')

@login_required
def confirmDonation(request):
	current_user = request.user
	print(request.GET['boiii'][14:-1])
	print(request.GET['wishlist'][17:-1])
	cur_boiii = Boiii()
	cur_boiii = Boiii.objects.get(book_id = request.GET['boiii'][14:-1])
	cur_wish = Wishlist.objects.get(id = request.GET['wishlist'][17:-1])
	cur_boiii.received = True
	cur_wish.count = cur_wish.count - 1;
	cur_boiii.save()
	if cur_wish.count > 0:
		cur_wish.save()
	else:
		cur_wish.delete()
	cur_book = Book.objects.get(pk = cur_boiii.isbn_id)
	cur_book.count = cur_book.count - 1
	cur_book.save()
	return redirect('home')


@login_required
def confirmRejection(request):
	current_user = request.user
	print(request.GET['boiii'][14:-1])
	print(request.GET['wishlist'][17:-1])
	cur_boiii = Boiii()
	cur_boiii = Boiii.objects.get(book_id = request.GET['boiii'][14:-1])
	cur_wish = Wishlist.objects.get(id = request.GET['wishlist'][17:-1])
	cur_boiii.donated = False
	cur_boiii.receiver_id_id = None
	cur_boiii.save()
	return redirect('home')


@login_required
def donate(request):
	form = UploadFileForm(request.POST, request.FILES)
	donate_isbn = request.POST['isbn']
	donate_condition = request.POST['condition']
	receiver_name = request.POST['username']
	donor_user = request.user
	donor = OurUser.objects.get(user = donor_user)
	donate_book = Boiii.objects.filter(isbn=donate_isbn, id=donor, donated=False)[0]
	donate_book.donated = True
	if form.is_valid(): 
		if 'Photo' in request.FILES:
			donate_book.photo = request.FILES['Photo']
	donate_book.condition=donate_condition
	donate_book.receiver_id=OurUser.objects.get(user_name=receiver_name) 
	donate_book.save()

	return redirect('home')

def about(request):
	return render(request,'about.html')


def contact(request):
	return render(request,'contact.html')

