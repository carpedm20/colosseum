from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'core.views.index', name='index'),
    url(r'^home/$', 'core.views.index', name='home'),
)
