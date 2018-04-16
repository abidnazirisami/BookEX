from django.shortcuts import render
from django.urls import *
from pages.models import Boiii, Book, Author
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz

@login_required
def displayList(request):
    book = Book.objects.all()
    return render(request, 'find/search_result.html', context={'book': book})

@login_required
def addToRequestQueue(request):
    use_isbns = request.POST.getlist('isbn', None)
    wishes=[]
    for use_isbn in use_isbns:
        if isbnlib.is_isbn10(use_isbn):
            use_isbn = isbnlib.to_isbn13(use_isbn)
            if isbnlib.is_isbn13(use_isbn):
                edition_list = isbnlib.editions(use_isbn, service='any')
                if(len(edition_list) != 0):
                    use_isbn = edition_list[0]
        if Wishlist.objects.filter(isbn=use_isbn).exists():
            wished = Wishlist.objects.get(isbn=use_isbn)
            wished.count+=1
            wished.save()
            wished.author_name=wished.author_name
            wishes.append(wished)
        else:
            requested_book = isbnlib.meta(use_isbn)
            authors = requested_book['Authors']
            author_string = bytes()
            isFirst = True
            for author in authors:
                if isFirst:
                    isFirst=False
                else:
                    author_string+=', '.encode('ascii', 'ignore')
                print(author)
                author_string+=author.encode('ascii','ignore')
            book_title = requested_book['Title']
            isAvail = False
            if Book.objects.filter(isbn=use_isbn).exists() :
                isAvail=True
            new_string = author_string.decode('utf-8')
            new_wish = Wishlist.objects.create(user= request.user, isbn=use_isbn, author_name=new_string, book_name=book_title, isAvailable=isAvail) 
            #new_wish.author_name=new_wish.author_name.decode('utf-8', 'ignore')
            wishes.append(new_wish)

    if not len(use_isbns) is 0:
        wishes.sort(key=lambda x: x.count ,reverse=True)
        return render(request, 'request/wishlist_added.html', context={'books': wishes})
    else:
        new_book = Book.objects.all()
        book_names=[]
        for new_books in new_book:
            book_names.append(new_books.book_name)
        return render(request, 'find/search_book.html', context={'books': book_names, 'error': "You didn't select any books :("})


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

        return render(request, 'request/search_result.html', context={'newbook': zip(new_list, author_name_list),'existingbook': zip(existing_list, existing_authors), 'exists':exists})
    else:
        new_book = Book.objects.all()
        book_names=[]
        for new_books in new_book:
            if not new_books.book_name in book_names:
                book_names.append(new_books.book_name)
        return render(request, 'find/search_book.html', context={'books': book_names, 'error': ""})

@login_required
def showWishlist(request):
    haswishes=False
    wishlist = []
    if Wishlist.objects.filter(user=request.user).exists():
        haswishes=True
        wishlist = Wishlist.objects.all().filter(user=request.user)
    return render(request, 'request/show_wishlist.html', context={'haswishes':haswishes, 'books': wishlist})
