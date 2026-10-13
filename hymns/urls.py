# from django.urls import path, include
# from rest_framework import routers
# from .views import HymnViewSet

# router = routers.DefaultRouter()
# router.register(r'hymns', HymnViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HymnViewSet, hymn_list, hymn_detail

# Router for online sync API
router = DefaultRouter()
router.register(r'hymns', HymnViewSet, basename='hymn')

urlpatterns = [
    # Offline templates (default Dholuo, Kiswahili selectable)
    path('hymns/', hymn_list, name='hymn_list'),
    path('hymns/<int:pk>/', hymn_detail, name='hymn_detail'),

    # Online sync API (only used when app fetches updates)
    path('api/', include(router.urls)),
]
