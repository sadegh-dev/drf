from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('one/', views.one ),
    #path('sayhello/', views.sayhello ),
    #path('persons/', views.persons ),
    #path('persond/<str:email>', views.person ),
    #path('create-person/', views.create_person ),
]
 

 # cedf21e7dc928cdaf1db4bbbc780bebe355a7f11