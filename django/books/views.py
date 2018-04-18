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
			use_isbn = request.POST['isbn']
			existing_book = Book.objects.get(isbn=use_isbn)
			existing_book.count = existing_book.count+1
			curUser = OurUser.objects.get(user = request.user)				
			curUser.donate_count = curUser.donate_count + 1
			existing_book.save()
			curUser.save()
			new_boi = Boiii.objects.create(id = curUser,isbn = existing_book)
			new_boi.save()
			return redirect('list_of_books')
		added_book = new_book.save(commit=False)
		use_isbn = isbnlib.clean(added_book.isbn)
		use_isbn = isbnlib.canonical(use_isbn)
		print(use_isbn)
		if isbnlib.is_isbn10(use_isbn):
			use_isbn = isbnlib.to_isbn13(use_isbn)
		if isbnlib.is_isbn13(use_isbn):
			edition_list = isbnlib.editions(use_isbn, service='any')
			if(len(edition_list) != 0):
				use_isbn = edition_list[0]
			if Book.objects.filter(isbn=use_isbn).exists():								
				existing_book = Book.objects.get(isbn=use_isbn)
				existing_book.count = existing_book.count+1
				curUser = OurUser.objects.get(user = request.user)				
				curUser.donate_count = curUser.donate_count + 1
				existing_book.save()
				curUser.save()
				new_boi = Boiii.objects.create(id = curUser,isbn = existing_book)
				new_boi.save()			
			else:
				find_book = isbnlib.meta(use_isbn)
				authors = find_book['Authors']
				book_publisher = find_book['Publisher']
				book_title = find_book['Title']
				book_date=1996
				if not find_book['Year'] is '':
					book_date = find_book['Year']
				add_author = Author.objects.create(author_name = authors)
				add_book = Book.objects.create(isbn = use_isbn,author_id = add_author,publisher = book_publisher,book_name = book_title,publish_year=book_date)
				curUser = OurUser.objects.get(user = request.user)
				new_boi = Boiii.objects.create(id = curUser,isbn = add_book)
				curUser.donate_count = curUser.donate_count + 1
				add_book.count = add_book.count+1
				add_book.save()
				add_author.save()
				curUser.save()
			return redirect('list_of_books')
		return render(request, 'books/donate_book.html', context = {'form':new_book,'error':"Enter a valid isbn"})
	else:
		new_book = AddBook()
		return render(request, 'books/donate_book.html', context = {'form':new_book,'error':""})

@login_required
def addNew(request):
    if request.method == "POST":
        form_book = AddNewBook(request.POST)
        form_author = AddAuthor(request.POST)
        if form_book.is_valid() and form_author.is_valid:
            book = form_book.save(commit=False)
            count = Author.objects.filter().count()
            print(count)
            author = Author.objects.create(author_name=request.POST['author_name'])
            author.save()
            book.author_id = author
            book.isbn = str(count)
            book.save()
            return redirect('home')
    else:
        form_book = AddNewBook()
        form_author = AddAuthor()
    return render(request, 'registration/edit_profile.html', {'form_profile': form_author, 'form_user': form_book})

@login_required
def viewBookProfile(request, req_isbn):
	current_book = Book()
	current_author = Author()
	if Book.objects.filter(pk=req_isbn).exists():
		current_book = Book.objects.get(pk = req_isbn)
	print(current_book.book_name)
	if Author.objects.filter(pk=current_book.author_id_id).exists():
		current_author = Author.objects.get(pk=current_book.author_id_id)
	return render(request, 'books/book_profile.html', context={'book': current_book, 'author': current_author, })
