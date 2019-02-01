from django.urls import path, include
from rest_framework import routers
from eventos.api.views import *

router = routers.DefaultRouter()


router.register(r'events', EventsList)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/events/user/<int:pk>', EventsList.as_view({"get": "getByUser"})),
    path('api/login/', login)
]