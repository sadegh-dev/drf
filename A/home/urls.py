from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('one/', views.one, name='one'),
    path('two/', views.two, name='two'),
    path('persons/', views.persons ),
    path('person/<str:email>', views.person ),
    path('create-person/', views.create_person ),
]
 