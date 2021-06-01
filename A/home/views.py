from rest_framework.response import Response
from rest_framework.decorators import api_view


#@api_view(['GET','POST'])
# default [GET]
@api_view() 
def one(request):
    data = {
        "name":"charlie"
    }
    return Response(data)