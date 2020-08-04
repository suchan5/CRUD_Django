from django.shortcuts import render, HttpResponse
from .models import Book

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
    all_books = Book.objects.all()  # this 'Book' is our model from 'models.py' power of ORM(Obect Relation Model). 맨 위에도 import해주삼
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })
