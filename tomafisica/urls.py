from . import views
from django.conf.urls import url

urlpatterns = [
        url(r'^tomafisica/(?P<codigo>\w+)', views.tomafisica1),


        url(r'^tomafisica/$', views.tomafisica),


#
    ]

