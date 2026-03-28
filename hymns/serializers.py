from rest_framework import serializers
from .models import Hymn

class HymnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hymn
        fields = ['id', 'title', 'lyrics', 'number']