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



def homepage(request):
	current_user = request.user
	
	if current_user.is_authenticated:
		if not OurUser.objects.filter(user = current_user).exists():
			current_user.first_name = current_user.username
			current_user.save()
			current_profile = OurUser.objects.create(user = current_user, user_name = current_user.username)
		else:
			current_profile = OurUser.objects.get(user = current_user)
		
		return render(request,'home.html')
	return render(request, 'home.html')

@login_required
def confirmDonation(request):
	current_user = request.user
	print(request.GET['boiii'])
	print(request.GET['wishlist'])
	cur_boiii = Boiii.objects.get(book_id = request.GET['boiii'])
	cur_wish = Wishlist.objects.get(id = request.GET['wishlist'])
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
	print(request.GET['boiii'])
	print(request.GET['wishlist'])
	cur_boiii = Boiii.objects.get(book_id = request.GET['boiii'])
	cur_wish = Wishlist.objects.get(id = request.GET['wishlist'])
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

def story(request):
	return render(request,'story.html')
'''need to pass boiii.book_id'''
@login_required
def dontDonate(request):
	current_user = request.user
	print(request.GET['boiii'])
	#print(request.GET['wishlist'])
	cur_boiii = Boiii.objects.get(book_id = request.GET['boiii'])
	cur_book = Book.objects.get(isbn = cur_boiii.isbn_id)
	cur_user = OurUser.objects.get(user = current_user)
	#cur_wish = Wishlist.objects.get(id = request.GET['wishlist'])
	cur_user.donate_count = cur_user.donate_count - 1
	
	cur_book.count = cur_book.count - 1
	cur_user.save()
	cur_book.save()
	cur_boiii.delete()
	return redirect('pending')
