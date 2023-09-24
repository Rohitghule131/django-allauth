from django.db import models
from utilities.mixins import ModelMixins


class Auther(ModelMixins):
    """
    Class for storing auther.
    """
    email = models.EmailField(null=True, blank=False)
    number = models.CharField(null=True, blank=False)
    last_name = models.CharField(null=False, blank=False)
    first_name = models.CharField(null=False, blank=False)


class Book(ModelMixins):
    """
    Class for create a book model.
    """
    book_name = models.CharField(null=False, blank=False)
    brand_name = models.CharField(null=True, blank=False)
    publication_name = models.CharField(null=True, blank=False)
    auther = models.ForeignKey(Auther, null=True, blank=False, on_delete=models.CASCADE, related_name="auther_book")

