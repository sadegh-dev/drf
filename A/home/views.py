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



@api_view(['GET','POST'])
def two(request):
    if request.method == 'POST' :
        name = request.data['name']
        dd = {
            'name' :f'your name is {name}'
        }
        return Response(dd)
    else :
        dd ={
            'name' : 'your name is guest'
        }
        return Response(dd)

