from . import views
from django.conf.urls import url
#dsadsdbhb
#sadadsdsadahjvbjvghvh
urlpatterns = [
        url(r'^$', views.bodegatrabajo),
        #url(r'^plantilla/$', views.formu),
        #url(r'^plantilla2/$', views.pec),
        #url(r'^bodega/$', views.bodega),

        url(r'^error/$', views.error),
        url(r'^bodegas/$', views.bodegatrabajo),

        #url(r'^subirgrupos/$', views.subirgrupos),
        #url(r'^subirsubgrupos/$', views.subirsubgrupos),
        #url(r'^subirdigitos/$', views.subirdigitos),

        url(r'^error3/$', views.error3),
        #url(r'^subirsubgrupos/$', views.subirgrupos),

#
    ]

