from eventos.api.models import *
from eventos.api.serializers import *
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework import status, viewsets

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EventsList(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    @action(methods=['post'], detail=True)
    def many(self, request, pk=None):
        events  = self.get_object()
        serializer = EventsSerializer(data=request.data, many=True)
        if serializer.is_valid():
            events.save()
            return Response({'status': 'Evento creado correctamente'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)