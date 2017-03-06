from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^odmen/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.start),
    url(r'^inspection/$', views.inspection),
    url(r'^star/$', views.star),
    url(r'^delError/$', views.delError),
    url(r'^delSave/$', views.delSave),
    url(r'^error-list/$', views.errors),
    url(r'^save/$', views.save),
    url(r'^login/$', views.login),
    url(r'^parser/$', views.parser),
    url(r'^show/([0-9]+)$', views.show),

    url(r'^show/$', views.show),
    url(r'^download/$', views.download),
    url(r'^download/([0-9]+)$', views.download),
    url(r'^editLan/$', views.editLan),
    url(r'show/([0-9]+)/tests/([0-9]+)/$', views.tests),
    url(r'show/([0-9]+)/base/([0-9]+)/$', views.base),
    url(r'show/([0-9]+)/training/([0-9]+)/$', views.training),
    url(r'^abcc/$', views.abcc),
]
