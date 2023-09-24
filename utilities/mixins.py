from django.db import models
from django.utils import timezone


class ModelMixins(models.Model):
    """
    Class for create mixins for Model.
    """
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        abstract = True


