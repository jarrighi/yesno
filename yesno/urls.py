from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yesno.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.question, name='question'),
    url(r'^answer/([0-9]+)/(yes|no)$', views.answer, name='answer'),
)
