from django.shortcuts import render
from pages.models import Boiii,Book,Author
from .forms import *
from django.shortcuts import redirect
import isbnlib
from django.contrib.auth.decorators import login_required


@login_required
def displayBooks(request):
	book = Book.objects.all()
	return render(request, 'find/search_result.html', context = {'book':book})

@login_required
def searchBook(request):
	if request.method == "POST":	
		keyword = SearchBook(request.POST)			
		search = request.POST['find_book']
		print(search)
		book_list = isbnlib.goom(search)
		new_list = list()
		author_name_list = list()
		for book in book_list:
			name = book['Authors']
			author = Author(author_name = name)
			add_book = Book(isbn = book['ISBN-13'],publisher = book['Publisher'],author_id = author,book_name = book['Title'],publish_year=book['Year'])
			author_name_list.append(author)
			new_list.append(add_book)
			
		return render(request,'find/search_result.html',context = {'book':zip(new_list,author_name_list)})
	else:
		new_book = SearchBook()
	return render(request, 'find/search_book.html', context = {'form':new_book,'error':"Enter a valid isbn"})

