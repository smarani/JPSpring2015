from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fpt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('foodpantry.urls', namespace='foodpantry')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)