from rest_framework import serializers

from .models import Auther


class ListAutherSerializer(serializers.ModelSerializer):
    """
    Class for create auther serializer.
    """

    class Meta:
        model = Auther
        fields = ("id", "first_name", "last_name", "email", "number", "created_at", "updated_at")
