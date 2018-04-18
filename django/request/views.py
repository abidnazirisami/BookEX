from django.shortcuts import render
from django.urls import *
from pages.models import Boiii, Book, Author
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from django.shortcuts import redirect
@login_required
def displayList(request):
    book = Book.objects.all()
    return render(request, 'request/search_result.html', context={'book': book})

@login_required
def addToRequestQueue(request):
    use_isbns = request.POST.getlist('isbn', None)
    wishes=[]
    cnt=0
    new_authors = request.POST.getlist('author_name', None)
    new_book_names = request.POST.getlist('book_name', None)
    new_counts = request.POST.getlist('count', None)
    for use_isbn in use_isbns:
        if isbnlib.is_isbn10(use_isbn):
            use_isbn = isbnlib.to_isbn13(use_isbn)
            if isbnlib.is_isbn13(use_isbn):
                edition_list = isbnlib.editions(use_isbn, service='any')
                if(len(edition_list) != 0):
                    use_isbn = edition_list[0]
        if Wishlist.objects.filter(isbn=use_isbn, user=request.user).exists():
            wished = Wishlist.objects.get(isbn=use_isbn, user=request.user)
            wished.count+=1
            wished.save()
            wished.author_name=wished.author_name
            wishes.append(wished)
        elif not isbnlib.is_isbn13(use_isbn):
            author_string = new_authors[cnt]
            book_title = new_book_names[cnt]
            isAvail = False

            new_wish = Wishlist.objects.create(user= request.user, isbn=use_isbn, author_name=author_string, book_name=book_title, isAvailable=isAvail) 
            if Book.objects.filter(isbn=use_isbn).exists() and int(float(new_counts[cnt])) > 0:
                isAvail=True
            else:
                Book.object.create(isbn=use_isbn, )
            wishes.append(new_wish)
            cnt+=1
        else:
            requested_book = isbnlib.meta(use_isbn)
            if requested_book is None:
                requested_book = isbnlib.goom(use_isbn)
                requested_book = requested_book[0]
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
            else:
                book_publisher = requested_book['Publisher']
                book_date = 1996
                if not requested_book['Year'] is '':
                    book_date = requested_book['Year']
                add_author = Author.objects.create(author_name=authors)
                Book.objects.create(isbn=use_isbn, author_id=add_author, publisher=book_publisher,
                                               book_name=book_title, publish_year=book_date)
            new_string = author_string.decode('utf-8')
            new_wish = Wishlist.objects.create(user= request.user, isbn=use_isbn, author_name=new_string, book_name=book_title, isAvailable=isAvail) 
            wishes.append(new_wish)

    if not len(use_isbns) is 0:
        wishes.sort(key=lambda x: x.count ,reverse=True)
        return render(request, 'request/wishlist_added.html', context={'books': wishes})
    else:
        new_book = Book.objects.all()
        book_names=[]
        for new_books in new_book:
            book_names.append(new_books.book_name)
        return render(request, 'request/search_book.html', context={'books': book_names, 'error': "You didn't select any books :("})


@login_required
def searchBook(request):
    haswishes=False
    wishlist = []
    if Wishlist.objects.filter(user=request.user).exists():
        haswishes=True
        wishlist = Wishlist.objects.all().filter(user=request.user)
    if request.method == "POST":
        search = request.POST.get('find_book',None)
        if search is None or search == '':
            new_book = Book.objects.all()
            book_names=[]
            for new_books in new_book:
                book_names.append(new_books.book_name)
            return render(request, 'request/search_book.html', context={'books': book_names, 'error': "Enter a valid keyword", 'wished_books' : wishlist, 'haswishes': haswishes})
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
                        if isFirst and c is '\'':
                            isFirst=False
                            isOdd=False
                        elif c is '\'' and isOdd and not isFirst:
                            cur_author_string+=','
                            isOdd=False
                        elif c is '\'' and not isOdd:
                            isOdd=True
                        else:
                            cur_author_string+=c
                existing_authors.append(cur_author_string)
                exists = True
        book_list = isbnlib.goom(search.encode('utf-8', 'replace').decode('ascii','ignore'))
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
        return render(request, 'request/search_book.html', context={'books': book_names, 'error': "", 'wished_books':wishlist, 'haswishes':haswishes})

@login_required
def showWishlist(request):
    haswishes=False
    wishlist = []
    if Wishlist.objects.filter(user=request.user).exists():
        haswishes=True
        wishlist = Wishlist.objects.all().filter(user=request.user)
    return render(request, 'request/show_wishlist.html', context={'haswishes':haswishes, 'books': wishlist})

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
            if 'photo' in request.FILES:
                book.photo = request.FILES['photo']
            book.save()
            return redirect('home')
    else:
        form_book = AddNewBook()
        form_author = AddAuthor()
    return render(request, 'registration/edit_profile.html', {'form_profile': form_author, 'form_user': form_book})
