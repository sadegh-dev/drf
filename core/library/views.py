from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers
from .models import Category, Author, Book 



# Test 1

@api_view(['GET','POST'])
def test(request):
    if request.method == 'GET':
        the_type = 'this is GET method'
    elif request.method == 'POST':
        the_type = 'this is POST method'
    
    return Response(the_type)


# Test 2

@api_view(['GET',])
def get_user_test(request):
    try :
        res = request.data['name']
    except :
        res = 'None'
    return Response(res)



# List catogory

@api_view(['GET',])
def list_category(request):
    books = Category.objects.all()
    ser_data = serializers.CategorySerializer(books, many=True)
    return Response(ser_data.data)



# List Authors

@api_view(['GET',])
def list_authors(request):
    authors = Author.objects.all()
    ser_data = serializers.AuthorSerializer(authors, many=True)
    return Response(ser_data.data)



# List Books

@api_view(['GET',])
def list_books(request):
    books = Book.objects.all()
    ser_data = serializers.BookSerializer(books, many=True)
    return Response(ser_data.data)




