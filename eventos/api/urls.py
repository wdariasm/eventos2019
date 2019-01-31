from django.urls import path, include
from rest_framework import routers
from eventos.api.views import *

router = routers.DefaultRouter()

router.register(r'category', CategoryList)
router.register(r'events', EventsList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/events/user/<int:pk>', EventsList.as_view({"get": "getByUser"}))
]