from django.db import models


class Book(models.Model):
    """
    - title - CharField
    - author - CharField
    - description - TextField
    - added - DateTimeField (auto)
    """

    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.title}" by {self.author}'