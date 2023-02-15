from django.db import models

# Create your models here.

class Book(models.Modal):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publisher_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
