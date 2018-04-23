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

def rate(request, isbn):
	print(isbn)
	print(request.user.username)
	return render(request, 'rating/ratings.html')