# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tomafisica.models import Bodegas
from .models import Unidades
from .models import ProductoBodega
admin.site.register(ProductoBodega)
admin.site.register(Unidades)


admin.site.register(Bodegas)