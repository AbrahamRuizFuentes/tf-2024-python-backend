from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_year = models.IntegerField()
    is_exclusive = models.BooleanField(default=False)

    def __str__(self):
        return self.title
