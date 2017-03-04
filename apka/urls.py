from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^odmen/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.start),
    url(r'^login/$', views.login),
    url(r'^parser/$', views.parser),
    url(r'^krok/([0-9]+)/show$', views.show),
    url(r'^editLan/$', views.editLan),
    url(r'([0-9]+)/show/tests/([0-9]+)/$', views.tests),
    url(r'([0-9]+)/show/base/([0-9]+)/$', views.base),
    url(r'([0-9]+)/show/training/([0-9]+)/$', views.training),
    url(r'^abcc/$', views.abcc),
]
