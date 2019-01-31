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

    @action( methods=['put'], detail=False)
    def put(self, request, pk=None):
        events = Events.objects.get( pk=pk )
        serializer = EventsSerializer( events, data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )

        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action( methods=['get'], detail=True )
    def getByUser(self, request, pk=None):
        events = Events.objects.filter(userId=pk ).order_by( '-id' )
        serializer = EventsSerializer( events, many=True )
        return Response( serializer.data )

    @action(methods=['post'], detail=True)
    def guardar(self, request):
        events = self.get_object()
        serializer = EventsSerializer(data=request.data, many=True)
        if serializer.is_valid():
            events.save()
            return Response({'status': 'Evento creado correctamente'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action( methods=['delete'], detail=False )
    def delete(self, request, pk=None):
        events = Events.objects.get( pk=pk )
        if (events.delete()):
            return Response( status=status.HTTP_200_OK )
        return Response(status=status.HTTP_204_NO_CONTENT)
