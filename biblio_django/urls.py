from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblio_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^buscar/',include('catalogo.urls')),
    url(r'^$','catalogo.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'catalogo.views.logout_view', name="vista_logout")
)
