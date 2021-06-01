from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer, PersonSerializer2
from .models import Person


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


@api_view()
def persons(reauest):
    pers = Person.objects.all()
    ser_data = PersonSerializer(pers, many = True)
    return Response(ser_data.data)



@api_view()
def person(request, email):
    try :
        the_person = Person.objects.get(email=email)
    except:
        return Response({'person':'does not exist'})
    ser_data = PersonSerializer2(the_person)
    return Response(ser_data.data) 



