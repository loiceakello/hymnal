# from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Hymn
# from .serializers import HymnSerializer
# from django.shortcuts import render


# class HymnViewSet(viewsets.ModelViewSet):
#     queryset = Hymn.objects.all()
#     serializer_class = HymnSerializer

#     # Add filtering and search
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['number']  # exact match filter
#     search_fields = ['title', 'lyrics']  # partial match search



from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hymn
from .serializers import HymnSerializer

class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all()
    serializer_class = HymnSerializer

    # Enable filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['number']  # exact match filter
    search_fields = ['title', 'lyrics']  # partial match search

    def get_queryset(self):
        qs = super().get_queryset()
        # Default to Dholuo hymns if no language is specified
        language = self.request.query_params.get('language', 'dholuo')
        updated_after = self.request.query_params.get('updated_after')

        # Filter hymns by language (one language at a time)
        qs = qs.filter(language=language)

        # Optional sync filter: only hymns updated after a timestamp
        if updated_after:
            qs = qs.filter(updated_at__gt=updated_after)

        return qs
