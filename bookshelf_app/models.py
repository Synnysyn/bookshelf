from django.db import models


class Book(models.Model):
    """
    Book model, to be finished
    """

    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.title}" by {self.author}'