from rest_framework import serializers
from .models import Persona

class PersonaSer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id','nombre','apellido']