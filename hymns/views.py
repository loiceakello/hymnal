from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hymn
from .serializers import HymnSerializer
from django.shortcuts import render


class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all()
    serializer_class = HymnSerializer

    # Add filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['number']  # exact match filter
    search_fields = ['title', 'lyrics']  # partial match search
