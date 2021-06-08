from django.db.models.query import QuerySet
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer2
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class PersonViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer2(QuerySet, many=True)
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonSerializer2(person)
        return Response(serializer.data)





