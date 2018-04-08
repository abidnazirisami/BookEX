from django.shortcuts import render
from pages.models import Boiii,Book,Author
from .forms import *
from django.shortcuts import redirect
import isbnlib
from django.contrib.auth.decorators import login_required


@login_required
def displayBooks(request):
	book = Book.objects.all()
	return render(request, 'books/list_of_books.html', context = {'book':book})

@login_required
def addBook(request):
	if request.method == "POST":	
		new_book = AddBook(request.POST)
		if not(new_book.is_valid()):			
			book_isbn = request.POST['isbn']
			book_ins = Book.objects.get(isbn=book_isbn)
			book_ins.count = book_ins.count+1
			book_ins.save()
			return redirect('list_of_books')
		added_book = new_book.save(commit=False)
		use_isbn = isbnlib.clean(added_book.isbn)
		new_isbn = isbnlib.canonical(use_isbn)
		print(use_isbn)
		if isbnlib.is_isbn10(use_isbn):
			use_isbn = isbnlib.to_isbn13(use_isbn)
		if isbnlib.is_isbn13(use_isbn):
			edition_list = isbnlib.editions(use_isbn)
			if(len(edition_list) != 0):
				use_isbn = edition_list[0]
			if Book.objects.filter(isbn=use_isbn).exists():
				existing_book = Book.objects.get(isbn=use_isbn)
				existing_book.count = existing_book.count+1
				existing_book.save()
			else:
				find_book = isbnlib.meta(use_isbn)
				authors = find_book['Authors']
				book_publisher = find_book['Publisher']
				book_title = find_book['Title']
				book_date = find_book['Year']
				add_author = Author.objects.create(author_name = authors)
				add_book = Book.objects.create(isbn = use_isbn,author_id = add_author,publisher = book_publisher,book_name = book_title,publish_year=book_date)
				add_book.count = add_book.count+1
				add_book.save()
				add_author.save()
			return redirect('list_of_books')
	else:
		new_book = AddBook()
	return render(request, 'books/donate_book.html', context = {'form':new_book,'error':"Enter a valid isbn"})

