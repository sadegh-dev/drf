from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('test1/',views.test) ,
    path('test2/',views.get_user_test) ,
    # List
    path('list-categories/',views.list_category) ,
    path('list-authors/',views.list_authors) ,
    path('list-books/',views.list_books) ,
    # Details
    path('category/<int:id>/',views.details_category) ,
    path('author/<str:email>/',views.details_author) ,
    # Add
    path('add-category/',views.add_category) ,
    # Delete
    path('delete-category/<int:id>/',views.delete_category) ,

]