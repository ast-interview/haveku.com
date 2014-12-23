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
        if obj.thumbnail=="" or obj.title=="" or obj.vid=="":
            
            result = parsevedio.get_data_from_web_interface(obj.url)
            try:
                if obj.vid=="":
                    obj.vid = parsevedio.get_vid_of_url(obj.url)
                if obj.title == "":
                    obj.title = result[0]
                if obj.description == "":
                    obj.description = result[1]
                if obj.thumbnail == "":
                    obj.thumbnail = result[2]
            except:
                pass
        
        obj.save()



admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Vedio, VedioAdmin)


