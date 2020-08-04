from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # this Book from 'models.py'
        # we use tuples here. Once you put in tuple, we cannot change anymore. immutable 
        fields = ('title', 'desc', 'ISBN', 'pageCount')
