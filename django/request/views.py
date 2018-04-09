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
        search = request.POST['find_book']
        print(search)
        new_list = list()
        author_name_list = list()
        book_table = Book.objects.all()
        for cur_book in book_table:
            if Author.objects.filter(pk=cur_book.author_id.author_id).exists():
                cur_author = Author.objects.get(pk=cur_book.author_id.author_id)
            cur_book_string = cur_book.isbn + " " + cur_book.publisher + " " + cur_author.author_name
            cur_book_string = cur_book_string + " " + cur_book.book_name + " " + str(cur_book.publish_year)
            print(cur_book_string)
            print(fuzz.token_set_ratio(cur_book_string, search))
            if fuzz.token_set_ratio(cur_book_string, search) > 40:
                new_list.append(cur_book)
        book_list = isbnlib.goom(search)
        for book in book_list:
            name = book['Authors']
            author = Author(author_name=name)
            add_book = Book(isbn=book['ISBN-13'], publisher=book['Publisher'], author_id=author,
                            book_name=book['Title'], publish_year=book['Year'])
            author_name_list.append(author)
            new_list.append(add_book)

        return render(request, 'find/search_result.html', context={'book': zip(new_list, author_name_list)})
    else:
        new_book = SearchBook()
    return render(request, 'find/search_book.html', context={'form': new_book, 'error': "Enter a valid isbn"})
