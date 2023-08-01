from rest_framework import serializers
from books.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "picture",
            "name",
            "price",
            "author",
            "year",
            "pages",
            "quantity",
            "avtive",
        ]
