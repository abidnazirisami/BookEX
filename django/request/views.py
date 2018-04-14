from django.shortcuts import render
from pages.models import Boiii, Book, Author
from .forms import *
import isbnlib
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz

@login_required
def displayList(request):
    book = Book.objects.all()
    return render(request, 'find/search_result.html', context={'book': book})


@login_required
def searchBook(request):
    if request.method == "POST":
        keyword = SearchBook(request.POST)
        search = request.POST.get('find_book','A')
        print(search)
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
                existing_authors.append(cur_author)
        book_list = isbnlib.goom(search)
        for book in book_list:
            name = book['Authors']
            author = Author(author_name=name)
            add_book = Book(isbn=book['ISBN-13'], publisher=book['Publisher'], author_id=author,
                            book_name=book['Title'], publish_year=book['Year'])
            author_name_list.append(author)
            new_list.append(add_book)

        return render(request, 'request/search_result.html', context={'newbook': zip(new_list, author_name_list),'existingbook': zip(existing_list, existing_authors)})
    else:
        new_book = Book.objects.all()
        book_names=[]
        for new_books in new_book:
            book_names.append(new_books.book_name)
        return render(request, 'find/search_book.html', context={'books': book_names, 'error': "Enter a valid isbn"})
