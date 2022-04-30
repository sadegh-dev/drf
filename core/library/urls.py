from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('test1/',views.test) ,
    path('test2/',views.get_user_test) ,
    path('list-category/',views.list_category) ,
    path('list-authors/',views.list_authors) ,
    path('list-books/',views.list_books) ,

]