from . import views
from django.conf.urls import url
#dsadsdbhb
#sadadsdsadahjvbjvghvh
urlpatterns = [

        url(r'^clases/$', views.clases),
        url(r'^catalogacion/confirmacion/(?P<codigo>\w+)', views.catalogacion5),
        url(r'^catalogacion/3digitos/(?P<codigo>\w+)', views.catalogacion4),
        url(r'^catalogacion/subgrupo/(?P<codigo>\w+)', views.catalogacion3),
        url(r'^catalogacion/grupo/(?P<codigo>\w+)', views.catalogacion2),
        # url(r'^tomafisica/(?P<codigo>\w+)', views.catalogacion2),
        url(r'^catalogacion/(?P<codigo>\w+)', views.catalogacion1),
        url(r'^catalogado/(?P<codigo>\w+)', views.catalogado),
        url(r'^catalogacion/$', views.catalogacion),

    #
    ]

