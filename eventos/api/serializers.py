from rest_framework import serializers
from eventos.api.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category,
        field = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    category  = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    class Meta:
        model = Events
        field = '__all__'
