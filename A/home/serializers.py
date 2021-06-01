from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.Serializer):
    id      = serializers.IntegerField()
    name    = serializers.CharField()
    age     = serializers.IntegerField()
    email   = serializers.EmailField()


class PersonSerializer2(serializers.ModelSerializer):
    class Meta :
        model = Person
        fields = ('id','name','age','email')
        extra_kwargs = {
            'email' : { 'write_only' : True, },
        }
