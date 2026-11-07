from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Hymn
from .serializers import HymnSerializer

# Offline template views
def hymn_list(request):
    language = request.GET.get('language', 'dholuo')
    hymns = Hymn.objects.filter(language=language).order_by('number')
    return render(request, 'hymn_list.html', {'hymns': hymns, 'language': language})

def hymn_detail(request, pk):
    hymn = get_object_or_404(Hymn, pk=pk)
    return render(request, 'hymn_detail.html', {'hymn': hymn})

# API ViewSet
class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all()
    serializer_class = HymnSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        language = self.request.query_params.get('language', 'dholuo')
        updated_after = self.request.query_params.get('updated_after')

        qs = qs.filter(language=language)
        if updated_after:
            qs = qs.filter(updated_at__gt=updated_after)
        return qs
