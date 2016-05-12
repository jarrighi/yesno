from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yesno.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.question, name='question'),
    url(r'^answer/(?P<qid>[0-9]+)/(?P<choice>yes|no)$', views.answer_ajax, name='answer_ajax'),
    url(r'^submit_q/$', views.submit_q, name='submit_q'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.loginview, name='login'),
    url(r'^logout/$', views.logoutview, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
)
