from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view



# Test 

@api_view(['GET','POST'])
def test(request):
    if request.method == 'GET':
        the_type = 'this is GET method'
    elif request.method == 'POST':
        the_type = 'this is POST method'
    
    return Response(the_type)


# Test

@api_view(['GET',])
def get_user_test(request):
    try :
        res = request.data['name']
    except :
        res = 'None'
    return Response(res)





