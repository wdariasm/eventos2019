from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from eventos.api.views import *

router = routers.DefaultRouter()

router.register(r'category', CategoryList)
router.register(r'events', EventsList)

urlpatterns = [
    path('api/', include(router.urls)),
]