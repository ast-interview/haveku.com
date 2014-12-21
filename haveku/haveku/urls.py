from django.conf.urls import patterns, include, url
from django.contrib import admin

#===============================================================================
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'haveku.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
# )
#===============================================================================
from . import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haveku.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',                              'vedios.views.index'),
    url(r'^tag-(?P<tag_id>\w+)/$',          'vedios.views.index'),
    url(r'^catalog-(?P<catalog_id>\w+)/$',  'vedios.views.index'),
    url(r'^search/',                        'vedios.views.index'),
    
    url(r'^vedio-(?P<vedio_id>\w+)/$',      'vedios.views.show'),
    
    url(r'^about/$',                        'vedios.views.about'),
    
    url(r'^admin/', include(admin.site.urls)),
)



handler404 = 'vedios.views.err404'
handler500 = 'vedios.views.err500'




















