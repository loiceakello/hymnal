# from django.contrib import admin
# from .models import Hymn

# admin.site.register(Hymn)



from django.contrib import admin
from .models import Hymn

@admin.register(Hymn)
class HymnAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'author', 'language', 'updated_at')

        # Add filters in the right sidebar
    list_filter = ('language',)

    # Enable search by title or lyrics
    search_fields = ('title', 'lyrics')

    # Order hymns by language then number
    ordering = ('language', 'number')
