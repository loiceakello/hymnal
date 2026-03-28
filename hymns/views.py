from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hymn
from .serializers import HymnSerializer
from django.shortcuts import render

def hymn_list(request):
    hymns = Hymn.objects.all().order_by("number")
    return render(request, "hymns/hymn_list.html", {"hymns": hymns})

def hymn_detail(request, hymn_id):
    hymn = Hymn.objects.get(id=hymn_id)
    return render(request, "hymns/hymn_detail.html", {"hymn": hymn})


class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all()
    serializer_class = HymnSerializer

    # Add filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['number']  # exact match filter
    search_fields = ['title', 'lyrics']  # partial match search
