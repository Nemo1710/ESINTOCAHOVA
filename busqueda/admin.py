# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Productos
#from tomafisica.models import Bodegas
from .models import ConfUsuario
from .models import Bodega


# Register your models here.


admin.site.register(Productos)

admin.site.register(ConfUsuario)
admin.site.register(Bodega)

