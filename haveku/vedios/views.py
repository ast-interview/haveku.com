from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404


from .models import Catalogue, Tag, Vedio


def index(request, tag_id="", catalog_id="", search=""):
    catalogues = Catalogue.objects.order_by('weight')
    tags       = Tag.objects.order_by('weight')
    
    try:
        search_data = None
        if 'search' in request.POST:
            search_data = request.POST['search']
            vedios = Vedio.objects.filter(title__contains=search_data).order_by('datetime').reverse()
        else:
            if tag_id == "" and catalog_id == "":
                vedios = Vedio.objects.order_by('datetime').reverse()
            else:
                if tag_id != "":
                    vedios = Vedio.objects.filter(tag__id__exact=tag_id).order_by('datetime').reverse()
                if catalog_id != "":
                    vedios = Vedio.objects.filter(tag__catalogue__id__exact=catalog_id).order_by('datetime').reverse()
    except Vedio.DoesNotExist:
        raise Http404
    
    active_catalogue = None
    
    try:
        if catalog_id != "":
            active_catalogue = Catalogue.objects.get(id=catalog_id)
    except Catalogue.DoesNotExist:
        raise Http404
    
    try:
        if tag_id != "":
            active_catalogue = Tag.objects.get(id=tag_id).catalogue
    except Tag.DoesNotExist:
        raise Http404
    
    
    active_tag = None
    if tag_id != "":
        active_tag = Tag.objects.get(id=tag_id)
    
    
    p = Paginator(vedios, 16)
    
    page = request.GET.get('page')
    try:
        vedios_this_page = p.page(page)
    except PageNotAnInteger:
        vedios_this_page = p.page(1)
    except EmptyPage:
        vedios_this_page = p.page(p.num_pages)
    
    
    context  = {'catalogues'      : catalogues,
                'tags'            : tags,
                'vedios'          : vedios_this_page,
                'activetag'       : active_tag,
                'active_catalogue': active_catalogue,
                'search_data'     : search_data,
                }
    
    return render(request, 'vedios/index.html', context)




def show(request, vedio_id=""):
    catalogues = Catalogue.objects.order_by('weight')
    tags       = Tag.objects.order_by('weight')
    
    try:
        vedio = Vedio.objects.get(id=vedio_id)
        active_tag = vedio.tag
    except Vedio.DoesNotExist:
        raise Http404
    
    context  = {'catalogues': catalogues,
                'tags'      : tags,
                'vedio'     : vedio,
                'activetag' : active_tag,
                }
    
    
    return render(request, 'vedios/show.html', context)

def about(request):
    catalogues = Catalogue.objects.order_by('weight')
    tags       = Tag.objects.order_by('weight')
    
    
    context  = {'catalogues': catalogues,
                'tags': tags,
                }
    
    
    return render(request, 'vedios/about.html', context)






def err404(request):
    catalogues = Catalogue.objects.order_by('weight')
    tags       = Tag.objects.order_by('weight')
    
    
    context  = {'catalogues': catalogues,
                'tags'      : tags,
                'err404'    : True,
                }
    
    return render(request, 'vedios/error.html', context)



def err500(request):
    catalogues = Catalogue.objects.order_by('weight')
    tags       = Tag.objects.order_by('weight')
    
    
    context  = {'catalogues': catalogues,
                'tags'      : tags,
                'err500'    : True,
                }
    
    
    return render(request, 'vedios/error.html', context)


















