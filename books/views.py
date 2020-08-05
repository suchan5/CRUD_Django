from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm  # class name from 'forms.py'

# Create your views here.
# A View (in other words, a view function) refers to a function.
# All view function must have the variable 'request' as their first argument.
# I also need to import HttpResponse, otherwise it won't work.  맨 위에다가 import 'HttpResponse'
# 그리고 또 Project folder (= BookReviewProject) 안에 있는 'urls.py' 로 가서 path 지정해 줘야함.
'''
def index(request):
    return HttpResponse(request)

이제 요놈은 뒤로하고 밑에처럼 바꿔주자 now we have template 이니께 ㅋ
'''


def index(request):
    fname = "Su Chan"
    lname = "Cho"
    return render(request, 'books/index.template.html', {
        'first_name': fname,
        'last_name': lname
    })


def show_books(request):
    # SELECT * FROM books;
    all_books = Book.objects.all()  # 맨 위에도 import해주삼. this 'Book' is our model from 'models.py' power of ORM(Obect Relation Model).
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })


def show_authors(request):
    all_authors = Author.objects.all()  # 맨 위에도 import 잊지마삼
    return render(request, 'books/all_authors.template.html', {
        'authors': all_authors
    })


def create_book(request):
    if request.method == "POST":
        print(request.POST)

        # create the BookForm by filling it with data from the users' submission
        create_form = BookForm(request.POST)

        if create_form.is_valid():
            # create a model based on the data in the form
            create_form.save()
            return redirect(reverse(show_books))
        else:
            return render(request, 'books/create_book.template.html', {
                'form': create_form
            })
    else:
        create_form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': create_form
        })


def create_author(request):
    if request.method == "POST":
        print(request.POST)

        create_form = AuthorForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(show_authors))
        else:
            return render(request, 'books/create_author.template.html', {
                'form': create_form
            })
    else:
        create_form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': create_form
        })


def update_book(request, book_id):
    # retrieve data from object(Book model we created) first
    book_being_updated = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(show_books))
        else:
            return render(request, 'books/update_book.template.html', {
                "form": book_form
            })
    else:
        # create a form with the book details filled in
        book_form = BookForm(instance=book_being_updated)
        return render(request, 'books/update_book.template.html', {
            "form": book_form
        })
