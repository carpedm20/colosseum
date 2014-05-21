from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'colosseum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^summernote/', include('django_summernote.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('core.urls', namespace='core')),
    url(r'^c/', include('post.urls', namespace='post')),
    url(r'^account/', include('account.urls', namespace='account')),

    url(r'/files/(?P<post_id>\d+)/upload/', 'file.views.upload', name = 'jfu_upload' ),
    url(r'/files/(?P<post_id>\d+)/delete/(?P<pk>\d+)$', 'file.views.upload_delete', name = 'jfu_delete' ),
    url(r'/files/$', 'file.views.view_file_list', name = 'view_file_list' ),

)
