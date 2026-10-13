# from django.contrib import admin
# from .models import Hymn

# admin.site.register(Hymn)



from django.contrib import admin
from .models import Hymn

@admin.register(Hymn)
class HymnAdmin(admin.ModelAdmin):
    # Show these fields in the admin list view
    list_display = ('number', 'title', 'author', 'language', 'updated_at')

    # Add filters in the right sidebar
    list_filter = ('language',)

    # Enable search by title or lyrics
    search_fields = ('title', 'lyrics')

    # Order hymns by language then number
    ordering = ('language', 'number')

    # Optional: group fields in the form
    fieldsets = (
        (None, {
            'fields': ('number', 'title', 'lyrics', 'language')
        }),
        ('Metadata', {
            'fields': ('updated_at',),
            'classes': ('collapse',),
        }),
    )


