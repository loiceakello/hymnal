# from django.urls import path, include
# from rest_framework import routers
# from .views import HymnViewSet

# router = routers.DefaultRouter()
# router.register(r'hymns', HymnViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]



from django.urls import path, include
from rest_framework import routers
from .views import HymnViewSet

# Router for online sync API
router = routers.DefaultRouter()
router.register(r'hymns', HymnViewSet, basename='hymn')

urlpatterns = [
    # Offline hymns: handled by bundled hymns.db in the app
    # These routes are for templates or local views if needed
    path('', include('hymns.urls')),

    # Online sync API: only called when app fetches updates
    path('api/', include(router.urls)),
]
