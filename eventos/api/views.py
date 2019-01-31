from eventos.api.models import *
from eventos.api.serializers import *
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EventsList(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('-id')
    serializer_class = EventsSerializer

    @action(methods=['post'], detail=True)
    def many(self, request, pk=None):
        events = self.get_object()
        serializer = EventsSerializer(data=request.data, many=True)
        if serializer.is_valid():
            events.save()
            return Response({'status': 'Evento creado correctamente'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def getByUser(self, request, pk=None):
        events = Events.objects.filter(userId=pk).order_by('-id')
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)