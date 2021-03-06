from django.db import models


class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

 
class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    pageCount = models.IntegerField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_Name = models.CharField(blank=False, max_length=50)
    last_Name = models.CharField(blank=False, max_length=50)
    date_of_birth = models.IntegerField(blank=False)
    # 'models.DataField(blank=False)'로 할 껄

    def __str__(self):
        return self.first_Name + " " + self.last_Name



