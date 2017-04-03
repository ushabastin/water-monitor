from django.contrib import admin
from .models import Nodename, Sensordata

class SensordataInline(admin.TabularInline):
    model = Sensordata
    extra = 3
    
class NodenameAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'was_published_recently')
    list_filter = ['published_date']
    search_fields = ['title']
    fieldsets = [
        (None  , {'fields': ['title']}), (None  , {'fields': ['text']}),
        ('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),
    ]
    inlines = [SensordataInline]
    


admin.site.register(Nodename, NodenameAdmin)


