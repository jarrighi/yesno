from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yesno.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.question, name='question'),
    url(r'^answer/(?P<qid>[0-9]+)/(?P<answer>yes|no)$', views.answer, name='answer'),
    url(r'^answers/(?P<qid>[0-9]+)', views.answer_tallies, name='answers'),
)
