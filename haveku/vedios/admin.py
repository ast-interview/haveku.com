from django.contrib import admin

from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.
from vedios.models import Catalogue, Tag, Vedio

from . import parsevedio


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
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'120'})},
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':120})},
    }
    
    def save_model(self, request, obj, form, change):
        '''
        if obj.provenance.domain == "youku.com":
            obj.image = thumbnail.preview_youku(obj.vid)
        elif obj.provenance.domain == "56.com":
            obj.image = thumbnail.previe_56(obj.vid)
        elif obj.provenance.domain == "tudou.com":
            obj.image = thumbnail.preview_tudou(obj.vid)
        else:
            obj.image = ""
        '''
        obj.image = ""
        obj.save()




admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Vedio, VedioAdmin)


