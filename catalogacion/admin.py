# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Clases
from .models import Grupos
from .models import SGrupo

admin.site.register(Clases)
admin.site.register(Grupos)
admin.site.register(SGrupo)
