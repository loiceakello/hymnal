# from rest_framework import serializers
# from .models import Hymn

# class HymnSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hymn
#         fields = ['id', 'title', 'lyrics', 'number']



from rest_framework import serializers
from .models import Hymn

class HymnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hymn
        fields = [
            'id',
            'number',
            'title',
            'lyrics',
            'language',     # include language so frontend can filter
            'updated_at'    # include updated_at for sync logic
        ]
