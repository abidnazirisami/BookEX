from django.shortcuts import render
from django.urls import *
from pages.models import *
from django.http import HttpResponseRedirect
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from django.shortcuts import redirect

def homepage(request):
	current_user = request.user
	if current_user.is_authenticated:
		if not OurUser.objects.filter(user=current_user).exists():
			current_user.first_name = current_user.username
			current_user.save()
			newUser = OurUser.objects.create(user = current_user,user_name = current_user.username)
	return render(request, 'home.html')