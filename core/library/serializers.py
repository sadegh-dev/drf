from rest_framework import serializers

from .models import Category, Author, Book


class CategorySerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    tbooks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    authors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'


