from django.shortcuts import render
from pages.models import Boiii,Book,Author
from .forms import *
from django.shortcuts import redirect
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz

@login_required
def displayBooks(request):
	book = Book.objects.all()
	return render(request, 'find/search_result.html', context = {'book':book})

@login_required
def searchBook(request):
    if request.method == "POST":
        search = request.POST.get('find_book',None)
        if search is None or search == '':
            new_book = Book.objects.all()
            book_names=[]
            for new_books in new_book:
                book_names.append(new_books.book_name)
            return render(request, 'find/search_book.html', context={'books': book_names, 'error': "Enter a valid keyword"})
        #print(search)
        exists = False
        new_list = list()
        existing_list = list()
        author_name_list = list()
        existing_authors = list()
        book_table = Book.objects.all()
        for cur_book in book_table:
            if Author.objects.filter(pk=cur_book.author_id.author_id).exists():
                cur_author = Author.objects.get(pk=cur_book.author_id.author_id)
            cur_book_string = cur_book.isbn + " " + cur_book.publisher + " " + cur_author.author_name
            cur_book_string = cur_book_string + " " + cur_book.book_name + " " + str(cur_book.publish_year)
            #print(cur_book_string)
            #print(fuzz.token_set_ratio(cur_book_string, search))
            if fuzz.token_set_ratio(cur_book_string, search) > 40:
                existing_list.append(cur_book)
                cur_author_string=''
                isOdd=True
                isFirst=True
                for c in cur_author.author_name:
                    if c is '[':
                        pass
                    elif c is ']':
                        pass
                    else:
                        if isFirst:
                            isFirst=False
                        elif c is '\'' and isOdd and not isFirst:
                            cur_author_string+=','
                            isOdd=False
                        elif c is '\'' and not isOdd:
                            isOdd=True
                        else:
                            cur_author_string+=c
                existing_authors.append(cur_author_string)
                exists = True
        book_list = isbnlib.goom(search)
        for book in book_list:
            name = book['Authors']
            author = Author(author_name=name)
            add_book = Book(isbn=book['ISBN-13'], publisher=book['Publisher'], author_id=author,
                            book_name=book['Title'], publish_year=book['Year'])
            author_string = ''
            isFirst=True
            for authors in author.author_name:
                if isFirst:
                    isFirst=False
                else:
                    author_string+=', '
                author_string += authors
            author_name_list.append(author_string)
            new_list.append(add_book)

        return render(request, 'find/search_result.html', context={'newbook': zip(new_list, author_name_list),'existingbook': zip(existing_list, existing_authors), 'exists':exists})
    else:
        new_book = Book.objects.all()
        book_names=[]
        for new_books in new_book:
            if not new_books.book_name in book_names:
                book_names.append(new_books.book_name)
        return render(request, 'find/search_book.html', context={'books': book_names, 'error': ""})
@login_required
def donate(request):
	if request.method == "POST":
		added_book = request.POST.getlist('isbn', None)
		for use_isbn in added_book:
			use_isbn = isbnlib.clean(use_isbn)
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
	else:
		new_book = Book.objects.all()
		book_names=[]
		for new_books in new_book:
			if not new_books.book_name in book_names:
				book_names.append(new_books.book_name)
		return render(request, 'find/search_book.html', context = {'books':book_names,'error':"Select a valid book"})


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
