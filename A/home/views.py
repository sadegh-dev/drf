from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .serializers import PersonSerializer, PersonSerializer2
from .models import Person
from rest_framework import status
from rest_framework.permissions import IsAdminUser



#@api_view(['GET','POST'])
# default [GET]
@api_view() 
def one(request):
    data = {
        "name":"charlie"
    }
    return Response(data)



@api_view(['GET','POST'])
def sayhello(request):
    if request.method == 'POST' :
        name = request.data['name']
        dd = {
            'name' :f'hello and welcome {name}'
        }
        return Response(dd)
    else :
        dd ={
            'name' : 'your are guest'
        }
        return Response(dd)



@api_view(['GET','POST'])
def persons(reauest):
    pers = Person.objects.all()
    ser_data = PersonSerializer(pers, many = True)
    return Response(ser_data.data, status = status.HTTP_200_OK )



@api_view()
@permission_classes([IsAdminUser,])
def person(request, email):
    try :
        the_person = Person.objects.get(email=email)
    except:
        return Response({'person':'does not exist'}, status = status.HTTP_404_NOT_FOUND )
    ser_data = PersonSerializer2(the_person)
    return Response(ser_data.data,  status = status.HTTP_200_OK ) 


@api_view(['POST'])
def create_person(request):
    info = PersonSerializer(data=request.data)
    if info.is_valid():
        info.save()
        context = {
            "message" : "OK"
        }
        return Response(context,status = status.HTTP_201_CREATED )
    else :
        return Response(info.errors)



