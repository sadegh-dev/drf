from rest_framework import serializers

class PersonSerializer(serializers.Serializers):
    name    = serializers.CharField()
    age     = serializers.IntegerField()
    email   = serializers.EmailField()