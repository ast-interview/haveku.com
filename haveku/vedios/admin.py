from django.contrib import admin

# Register your models here.
from vedios.models import Catalogue, Tag, Vedio



class CatalogueAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight')
    ordering     = ['weight']



class TagAdmin(admin.ModelAdmin):
    list_display = ('catalogue', 'name', 'weight')
    ordering     = ['weight']



class VedioAdmin(admin.ModelAdmin):
    list_display = ['tag', 'title', 'url']
    list_filter  = ['tag', 'datetime']
    ordering     = ['-datetime']

admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Vedio, VedioAdmin)


