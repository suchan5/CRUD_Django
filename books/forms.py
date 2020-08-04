from django import forms
from .models import Book, Author  # 요거 잊지마


class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # this Book from 'models.py'
        # we use tuples here. Once you put in tuple, we cannot change anymore. immutable 
        fields = ('title', 'desc', 'ISBN', 'pageCount')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author  # 맨 위에다가도 적어줘야함
        fields = ('first_Name', 'last_Name', 'date_of_birth')

