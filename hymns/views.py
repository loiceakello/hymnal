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



from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Hymn
from .serializers import HymnSerializer

# 🔹 Offline template views
def hymn_list(request):
    # Default to Dholuo hymns if no language is specified
    language = request.GET.get('language', 'dholuo')
    hymns = Hymn.objects.filter(language=language).order_by('number')
    return render(request, 'hymn_list.html', {'hymns': hymns, 'language': language})

def hymn_detail(request, pk):
    hymn = get_object_or_404(Hymn, pk=pk)
    return render(request, 'hymn_detail.html', {'hymn': hymn})

# 🔹 API ViewSet for sync (no filters/search)
class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all()
    serializer_class = HymnSerializer

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

