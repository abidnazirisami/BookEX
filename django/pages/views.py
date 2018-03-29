from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Author

def homePageView(request):
    return HttpResponse('This project will be turned into BookEX. Stay tuned!')
def displayTable(request):
	newauth = Author.objects.all()
	return render(request, "pages/test.html", context= {'book': newauth})
