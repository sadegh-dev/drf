from django.test import TestCase

# Create your tests here.



"""
views.py

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ExamleView(APIView):
    authentication_class = [SessionAuthentication, BasicAuthentication]
    ...

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def example_view(requeset):
    ...

"""

