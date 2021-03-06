from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^prop30/', include('prop30.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^score/(\w+)', 'prop30.views.data'),
    (r'^save/(\w+)', 'prop30.views.save'),
    (r'^save/$', 'prop30.views.save'),
    (r'^$', 'prop30.views.index'),
)

if settings.DEBUG:
    urlpatterns += static(settings.BOOTSTRAP_URL, document_root=settings.BOOTSTRAP_DIR)

urlpatterns += patterns('',
    (r'^(\w+)', 'prop30.views.index'),
)
