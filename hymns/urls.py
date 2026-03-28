from django.urls import path, include
from rest_framework import routers
from .views import HymnViewSet

router = routers.DefaultRouter()
router.register(r'hymns', HymnViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

