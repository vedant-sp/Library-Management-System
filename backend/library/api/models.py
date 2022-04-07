from django.db import models
from django.conf import settings

# Create your models here.
# BOOKS

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name