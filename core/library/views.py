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



# List Catogories

@api_view(['GET',])
def list_category(request):
    categories = Category.objects.all()
    ser_data = serializers.CategorySerializer(categories, many=True)
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



# details Category

@api_view(['GET',])
def details_category(request, id):
    try:
        the_category = Category.objects.get(id = id)
    except:
        return Response({'category':'Not exists'})
    ser_data = serializers.CategorySerializer(the_category)
    return Response(ser_data.data)



# details Authors [by Validation email]

@api_view(['GET',])
def details_author(request, email):
    try:
        the_author = Author.objects.get(email = email)
    except:
        return Response({'author':'Not exists'})
    ser_data = serializers.AuthorSerializer(the_author)
    return Response(ser_data.data)

