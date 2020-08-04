from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Author
from .forms import BookForm  # class name from 'forms.py'

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
    # check if we are submitting the form
    if request.method == "POST":
        print(request.POST)

        # create the BookForm by filling it with data from the users' submission
        create_form = BookForm(request.POST)
        # create a model based on the data in the form
        create_form.save()
        return redirect(reverse(show_books))

    else:
        create_form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': create_form
        })
