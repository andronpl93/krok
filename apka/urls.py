from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^odmen/', admin.site.urls),
    url(r'^$', views.start),
    url(r'^parser/$', views.parser),
]
